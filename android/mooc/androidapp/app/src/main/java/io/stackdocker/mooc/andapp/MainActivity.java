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

public class MainActivity  extends AppCompatActivity {
    private static final String TAG = MainActivity.class.getSimpleName();
    private static final String API_PATH = "http://192.168.0.20:8080/apis";

    private AsyncHttpClient client;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        client = new AsyncHttpClient();
        client.get(API_PATH, new AsyncHttpResponseHandler() {
            @Override
            public void onStart() {
                // called before request is started
                System.out.println("started");
            }

            @Override
            public void onSuccess(int statusCode, Header[] headers, byte[] response) {
                // called when response HTTP status is "200 OK"
                Log.i(TAG, response.toString());
                System.out.println(response.toString());
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

        final Button b = (Button)findViewById(R.id.my_button);
        b.setOnClickListener(new View.OnClickListener() {
            public void onClick(View arg0) {

                b.setClickable(false);

                Log.i(TAG, "clicked");

                client.get(API_PATH, new AsyncHttpResponseHandler() {
                    @Override
                    public void onStart() {
                        // called before request is started
                        System.out.println("started");
                    }

                    @Override
                    public void onSuccess(int statusCode, Header[] headers, byte[] response) {
                        // called when response HTTP status is "200 OK"
                        Log.i(TAG, response.toString());
                        System.out.println(response.toString());
                        if (response!=null) {
                            EditText et = (EditText)findViewById(R.id.my_edit);


                            et.setText(response.toString());


                        }
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

                new LongRunningGetIO().execute();
            }

                             }
        );
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
            HttpGet httpGet = new HttpGet(API_PATH);
            String text = null;
            try {
                HttpResponse response = httpClient.execute(httpGet, localContext);


                HttpEntity entity = response.getEntity();


                text = getASCIIContentFromEntity(entity);


            } catch (Exception e) {
                return e.getLocalizedMessage();
            }

            Log.i(TAG, text);
            System.out.println(text);
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
