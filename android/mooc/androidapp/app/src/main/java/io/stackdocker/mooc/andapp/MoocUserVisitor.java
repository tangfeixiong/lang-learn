package io.stackdocker.mooc.andapp;

import android.preference.PreferenceActivity;

import org.json.*;
import com.loopj.android.http.*;

/**
 * Created by fanhongling on 18/3/22.
 */

public class MoocUserVisitor {
    public void getPublicTimeline() throws JSONException {
        MoocApiClient.get("statuses/public_timeline.json", null, new JsonHttpResponseHandler() {

            public void onSuccess(int statusCode, PreferenceActivity.Header[] headers, JSONObject response) {
                // If the response is JSONObject instead of expected JSONArray
            }


            public void onSuccess(int statusCode, PreferenceActivity.Header[] headers, JSONArray timeline) {
                // Pull out the first event on the public timeline
                JSONObject firstEvent = null;
                String tweetText = "";
                try {
                    firstEvent = (JSONObject) timeline.get(0);
                    tweetText = firstEvent.getString("text");
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                // Do something with the response
                System.out.println(tweetText);
            }
        });
    }

}
