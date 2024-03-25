package com.example.readen

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ImageButton
import android.content.Intent
import android.widget.TextView

class AnswerActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_answer)

        val homeButton = findViewById<ImageButton>(R.id.HomeButton)
        homeButton.setOnClickListener {
            val intentHome = Intent(this, MainActivity::class.java)
            startActivity(intentHome)
        }

        val answerList = intArrayOf(1, 5, 2)
        val optionList = arrayOf("S V","S V O","S V C","S V O O","S V O C")
        val quizNo = intent.getIntExtra("quizNo", 1)
        val optionNo = intent.getIntExtra("optionNo", 1)
        val quizResultText = findViewById<TextView>(R.id.QuizResult)
        val answersText = findViewById<TextView>(R.id.AnswersText)
        if (optionNo == answerList[quizNo-1]) {
            quizResultText.text = "Q.${quizNo} :　正解！ (≧▽≦)"
        } else {
            quizResultText.text = "Q.${quizNo} :　不正解！ (T＿T)"
        }
        answersText.text = "正解 : ${optionList[answerList[quizNo-1]-1]}\n貴方の回答 : ${optionList[optionNo-1]}"
    }
}
