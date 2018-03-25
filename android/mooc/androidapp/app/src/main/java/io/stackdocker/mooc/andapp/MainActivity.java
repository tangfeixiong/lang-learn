package io.stackdocker.mooc.andapp;

import android.preference.PreferenceActivity;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import android.os.AsyncTask;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.type.CollectionType;
import com.fasterxml.jackson.databind.type.MapType;
import com.fasterxml.jackson.databind.type.TypeFactory;
import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.AsyncHttpResponseHandler;

import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;

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
    //private static final String API_PATH = "http://192.168.0.20:8080/apis";
    private String API_HOST;
    private String APIS_PATH;
    private String TOP_CLASS_PATH;

    private RecyclerView mRecyclerView;
    private RecyclerView.Adapter mAdapter;
    private RecyclerView.LayoutManager mLayoutManager;

    public static class MyClass {
        @JsonProperty
        private long id;
        @JsonProperty
        private String kind;
        @JsonProperty
        private String name;
        @JsonProperty
        private String tag;

        public String toString() {
            return name;
        }
    }
    private ArrayList<MyClass> myDataset;

    private AsyncHttpClient client;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        API_HOST = getResources().getString(R.string.api_host);
        APIS_PATH = API_HOST + "/apis";
//    TOP_CLASS_PATH = Paths.get(API_HOST,
//            "api/v1alpha", getResources().getString(R.string.top_classes_path)).toString();
        TOP_CLASS_PATH = API_HOST +
                "/api/v1alpha/namespaces/default/" + getResources().getString(R.string.top_classes_path);

        mRecyclerView = (RecyclerView) findViewById(R.id.my_recycler_view);

        // use this setting to improve performance if you know that changes
        // in content do not change the layout size of the RecyclerView
        mRecyclerView.setHasFixedSize(true);

        // use a linear layout manager
        mLayoutManager = new LinearLayoutManager(this);
        mRecyclerView.setLayoutManager(mLayoutManager);

        myDataset = new ArrayList<MyClass>();
        // specify an adapter (see also next example)
        mAdapter = new MyAdapter(myDataset);
        mRecyclerView.setAdapter(mAdapter);

        client = new AsyncHttpClient();

        final Button b1 = (Button)findViewById(R.id.my_button1);
        b1.setOnClickListener(new View.OnClickListener(){
            public void onClick(View arg0) {
                client.get(APIS_PATH, new AsyncHttpResponseHandler() {
                    @Override
                    public void onStart() {
                        // called before request is started
                    }

                    @Override
                    public void onSuccess(int statusCode, Header[] headers, byte[] response) {
                        // called when response HTTP status is "200 OK"
                        if (response!=null) {
                            EditText et = (EditText)findViewById(R.id.my_edit);


                            et.setText(new String(response));


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


            }
        });

        final Button b = (Button)findViewById(R.id.my_button);
        b.setOnClickListener(new View.OnClickListener() {
            public void onClick(View arg0) {

                client.get(TOP_CLASS_PATH, new AsyncHttpResponseHandler() {
                    @Override
                    public void onStart() {
                        // called before request is started
                        Log.i(TAG, "onStart");
                        System.out.println("onStart");
                    }

                    @Override
                    public void onSuccess(int statusCode, Header[] headers, byte[] response) {
                        // called when response HTTP status is "200 OK"
                        Log.i(TAG, "onSuccess");
                        System.out.println(response.toString());

                        if (response != null && response.length > 0) {
                            ObjectMapper mapper = new ObjectMapper();
                            TypeFactory typeFactory = mapper.getTypeFactory();
                            CollectionType mapType = typeFactory.constructCollectionType(ArrayList.class, MyClass.class);
                            try {
                                myDataset = mapper.readValue(new String(response), mapType);
                                mAdapter = new MyAdapter(myDataset);
                                mRecyclerView.setAdapter(mAdapter);
                            } catch (IOException e) {
                                e.printStackTrace();
                            }
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
                        Log.i(TAG, "onRetry");
                        System.out.println("onRetry");
                    }

                    public void onProgress(int bytesWritten, int totalSize) {
                        // Progress notification
                        Log.i(TAG, "onProgress");
                        System.out.println("onProgress");
                    }

                    @Override
                    public void onFinish() {
                        // Completed the request (either success or failure)
                        Log.i(TAG, "onFinish");
                        System.out.println("onFinish");
                    }

                });


                //b.setClickable(false);
                //new LongRunningGetIO().execute();
            }

                             });
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
            HttpGet httpGet = new HttpGet(APIS_PATH);
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
