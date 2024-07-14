import streamlit as st
import facebook_business
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.advideo import AdVideo
import tempfile

from models.credentials import Credentials

# # Facebook API setup
# ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
# AD_ACCOUNT_ID = "YOUR_AD_ACCOUNT_ID"
# APP_ID = "YOUR_APP_ID"
# APP_SECRET = "YOUR_APP_SECRET"

FacebookAdsApi.init(access_token=Credentials.ACCESS_TOKEN)


def upload_video_to_facebook(video_path):
    video = AdVideo(parent_id=Credentials.AD_ACCOUNT_ID)
    video[AdVideo.Field.name] = "Test Video"
    video[AdVideo.Field.filepath] = video_path
    video.remote_create()
    return video


def get_ad_data(ad_account_id):
    ad_account = AdAccount(ad_account_id)
    campaigns = ad_account.get_campaigns(
        fields=["name", "status", "objective", "created_time", "insights"]
    )
    return campaigns


def main():
    st.title("Video Upload and Facebook Ads Integration")

    uploaded_file = st.file_uploader(
        "Choose a video...", type=["mp4", "avi", "mov", "mkv"]
    )

    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())

        st.video(tfile.name)

        if st.button("Upload to Facebook Ads"):
            video = upload_video_to_facebook(tfile.name)
            st.success(f"Video uploaded successfully with ID: {video['id']}")

    if st.button("Get Ad Data and UTM Trackers"):
        ad_data = get_ad_data(Credentials.AD_ACCOUNT_ID)
        for campaign in ad_data:
            st.write(f"Campaign Name: {campaign['name']}")
            st.write(f"Status: {campaign['status']}")
            st.write(f"Objective: {campaign['objective']}")
            st.write(f"Created Time: {campaign['created_time']}")
            if "insights" in campaign:
                insights = campaign["insights"]
                for insight in insights:
                    st.write(f"Impressions: {insight['impressions']}")
                    st.write(f"Clicks: {insight['clicks']}")
                    st.write(f"Spend: {insight['spend']}")
                    st.write(f"UTM Source: {insight['utm_source']}")
                    st.write(f"UTM Medium: {insight['utm_medium']}")
                    st.write(f"UTM Campaign: {insight['utm_campaign']}")
                    st.write(f"UTM Content: {insight['utm_content']}")


if __name__ == "__main__":
    main()
