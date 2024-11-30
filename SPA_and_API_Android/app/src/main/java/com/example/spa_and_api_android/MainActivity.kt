package com.example.spa_and_api_android

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.webkit.WebView
import android.webkit.WebViewClient
import android.webkit.WebChromeClient

class AppWebViewClient: WebViewClient() {

    override fun shouldOverrideUrlLoading(view: WebView?, url: String?): Boolean {
        return false
    }

}

class MainActivity: AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val appWebView: WebView = findViewById<WebView>(R.id.AppWebView)
        appWebView.settings.allowFileAccess = true
        appWebView.settings.javaScriptEnabled = true
        appWebView.settings.domStorageEnabled = true
        appWebView.webViewClient = AppWebViewClient()
        appWebView.webChromeClient = WebChromeClient()
        appWebView.loadUrl("file:///android_asset/index.html")
    }
    
}
