package io.stackdocker.mooc.andapp;

import android.preference.PreferenceActivity;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import android.os.AsyncTask;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;

import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.AsyncHttpResponseHandler;

import java.io.IOException;
import java.io.InputStream;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.protocol.BasicHttpContext;
import org.apache.http.protocol.HttpContext;

import cz.msebera.android.httpclient.Header;

public class MainActivity  extends AppCompatActivity  implements OnClickListener {
    private static final String TAG = MainActivity.class.getSimpleName();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        AsyncHttpClient client = new AsyncHttpClient();
        client.get("http://127.0.0.1:8080/apis", new AsyncHttpResponseHandler() {
            @Override
            public void onStart() {
                // called before request is started
            }

            @Override
            public void onSuccess(int statusCode, Header[] headers, byte[] response) {
                // called when response HTTP status is "200 OK"
                Log.d(TAG, response.toString());
            }

            @Override
            public void onFailure(int statusCode, Header[] headers, byte[] errorResponse, Throwable e)
            {
                e.printStackTrace();
            }

            @Override
            public void onRetry(int retryNo) {
                // Request was retried
            }

            public void onProgress(int bytesWritten, int totalSize) {
                // Progress notification
            }

            @Override
            public void onFinish() {
                // Completed the request (either success or failure)
            }

        });
    }

    @Override
    public void onClick(View arg0) {
        Button b = (Button)findViewById(R.id.my_button);


        b.setClickable(false);
        new LongRunningGetIO().execute();
    }

    private class LongRunningGetIO extends AsyncTask <Void, Void, String> {
        protected String getASCIIContentFromEntity(HttpEntity entity) throws IllegalStateException, IOException {
            InputStream in = entity.getContent();


            StringBuffer out = new StringBuffer();
            int n = 1;
            while (n>0) {
                byte[] b = new byte[4096];
                n =  in.read(b);


                if (n>0) out.append(new String(b, 0, n));
            }


            return out.toString();
        }


        @Override


        protected String doInBackground(Void... params) {
            HttpClient httpClient = new DefaultHttpClient();
            HttpContext localContext = new BasicHttpContext();
            HttpGet httpGet = new HttpGet("http://127.0.0.1:8080/apis");
            String text = null;
            try {
                HttpResponse response = httpClient.execute(httpGet, localContext);


                HttpEntity entity = response.getEntity();


                text = getASCIIContentFromEntity(entity);


            } catch (Exception e) {
                return e.getLocalizedMessage();
            }


            return text;
        }


        protected void onPostExecute(String results) {
            if (results!=null) {
                EditText et = (EditText)findViewById(R.id.my_edit);


                et.setText(results);


            }


            Button b = (Button)findViewById(R.id.my_button);


            b.setClickable(true);
        }


    }

}
