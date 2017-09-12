package com.example.asus.sensordataserver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.TimeUnit;

import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.app.Activity;
import android.content.Context;
import android.view.Menu;
import android.widget.TextView;

public class MainActivity extends Activity {
    private static final String TAG="MainActivity";
    private SensorManager sensorManager;
    private float[] accelerometer_values=null;
    private float[] magnitude_values=null;
    public static TextView mTextView, textView1;
    private String IP = "";
    String buffer = "";
    public String pitchs="";
    public String yaws="";
    public double pitch;
    public double yaw;
    OutputStream output;
    private static ServerSocket serverSocket = null;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        sensorManager = (SensorManager) getSystemService(SENSOR_SERVICE);
        mTextView = (TextView) findViewById(R.id.textsss);
        textView1 = (TextView) findViewById(R.id.textView1);
        IP = getlocalip();
        textView1.setText("IP addresss:" + IP);

    }

    protected  void onResume(){
        super.onResume();
        boolean enable=sensorManager.registerListener(listener,sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER), SensorManager.SENSOR_DELAY_UI)
                &&sensorManager.registerListener(listener,sensorManager.getDefaultSensor(Sensor.TYPE_MAGNETIC_FIELD),SensorManager.SENSOR_DELAY_UI);
        if(!enable){
            sensorManager.unregisterListener(listener);
            //log.e(TAG,getString(R.string.msg_SensorNotSupported));
        }
    }
    protected void onPause()
    {
        super.onPause();
        //    sensorManager.unregisterListener(listener);
    }
    SensorEventListener listener=new SensorEventListener() {
        @Override
        public void onSensorChanged(SensorEvent event) {
            switch (event.sensor.getType()){
                case Sensor.TYPE_ACCELEROMETER:
                    accelerometer_values=event.values.clone();
                    break;
                case Sensor.TYPE_MAGNETIC_FIELD:
                    magnitude_values=event.values.clone();
                    break;
                default:
                    break;
            }
            if(magnitude_values==null||accelerometer_values==null)
            {
                return;
            }
            float[]R=new float[9];
            float[]values=new float[3];
            SensorManager.getRotationMatrix(R,null,accelerometer_values,magnitude_values);
            SensorManager.getOrientation(R,values);
            pitch=Math.toDegrees(values[2]);
            pitchs=""+pitch;
            yaw=Math.toDegrees(values[0]);
            yaws=""+yaw;
            pitchs=pitchs.substring(0,6);
            yaws=yaws.substring(0,6);
            new Thread() {
                public void run() {
                    try {
                        serverSocket = new ServerSocket(30000);
                        while (true) {
                            try {
                                Socket socket = serverSocket.accept();
                                output = socket.getOutputStream();
                                while(true) {
                                    output.write(("st"+pitchs+yaws+"\r\n").getBytes("UTF-8"));
                                    output.flush();
                                    //System.out.println(yaws);
                                   try
                                    {
                                        Thread.sleep(20);
                                    }
                                    catch(InterruptedException ex)
                                    {
                                        Thread.currentThread().interrupt();
                                    }
                                }
                            } catch (IOException e) {
                                e.printStackTrace();
                            }
                        }
                    } catch (IOException e1) {
                        // TODO Auto-generated catch block
                        e1.printStackTrace();
                    }
                };
            }.start();
            mTextView.setText("pitch:"+pitchs+"\nyaw:"+yaws);
        }
        @Override
        public void onAccuracyChanged(Sensor sensor, int i) {

        }
    };
    /**
     * 或取本机的ip地址
     */
    private String getlocalip(){
        WifiManager wifiManager = (WifiManager) getApplicationContext().getSystemService(Context.WIFI_SERVICE);
        WifiInfo wifiInfo = wifiManager.getConnectionInfo();
        int ipAddress = wifiInfo.getIpAddress();
        //  Log.d(Tag, "int ip "+ipAddress);
        if(ipAddress==0)return null;
        return ((ipAddress & 0xff)+"."+(ipAddress>>8 & 0xff)+"."
                +(ipAddress>>16 & 0xff)+"."+(ipAddress>>24 & 0xff));
    }

}

