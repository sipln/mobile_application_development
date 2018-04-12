package com.example.sipln.currencyconverter;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.*;

import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final EditText editText = (EditText) findViewById(R.id.et_1);
        final TextView textView = (TextView) findViewById(R.id.tv_KQ);

        final TextView tv_1 = (TextView) findViewById(R.id.tv_1);
        final TextView tv_2 = (TextView) findViewById(R.id.tv_2);

        final List<String> Monetary_Unit = new ArrayList<>();
        Monetary_Unit.add(tv_1.getText().toString());
        Monetary_Unit.add(tv_2.getText().toString());

        Button btnExchange = (Button) findViewById(R.id.btn_Exchange);
        btnExchange.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (tv_1.getText().toString() == Monetary_Unit.get(0)) {
                    tv_1.setText(Monetary_Unit.get(1));
                    tv_2.setText(Monetary_Unit.get(0));
                }
                else {
                    tv_1.setText(Monetary_Unit.get(0));
                    tv_2.setText(Monetary_Unit.get(1));
                }
            }
        });

        Button btnConverter = (Button) findViewById(R.id.btn_Converter);
        btnConverter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String amount = editText.getText().toString();
                double convertFactor = 22727.2727;
                Locale locale = new Locale("vi", "VN");
                NumberFormat numberFormat = NumberFormat.getNumberInstance(locale);

                if(tv_1.getText().toString()==Monetary_Unit.get(0))
                {

                    textView.setText(""+numberFormat.format(CurrencyConverter(Double.parseDouble(amount), convertFactor)));
                }
                else {
                    textView.setText(""+numberFormat.format(CurrencyConverter(Double.parseDouble(amount), 1/convertFactor)));
                }
            }
        });

    }

    private double CurrencyConverter(double amount, double converFactor) {
        return converFactor*amount;
    }

}
