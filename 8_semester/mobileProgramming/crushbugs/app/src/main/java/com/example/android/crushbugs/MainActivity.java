package com.example.android.crushbugs;

import android.animation.AnimatorSet;
import android.animation.ObjectAnimator;
import android.os.Bundle;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

import java.util.Random;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        start();

    }

    void start() {

        RelativeLayout window = findViewById(R.id.window);

        Handler handler = new Handler();

        String messageText = "Smashed";

        final int BUG_LIMIT = 12;

        handler.post(new Runnable() {

            int bugCount = 0;

            @Override
            public void run() {

                int height = window.getHeight();
                int width = window.getWidth();
                { // FIXME
                    height = (height == 0) ? 100 : height;
                    width = (width == 0) ? 100 : width;
                }
                for (int i = 0; i < 3; i++) {

                    if (bugCount >= BUG_LIMIT) {
                        continue;
                    }

                    bugCount++;

                    ImageView image = new ImageView(MainActivity.super.getBaseContext());

                    image.setImageResource(R.drawable.bug);

                    image.setX((float) getRand(width));
                    image.setY((float) getRand(height));

                    window.addView(image);

                    image.setOnClickListener((e) -> {

                        bugCount--;

                        window.removeView(image);

                        TextView message = new TextView(MainActivity.super.getBaseContext());

                        message.setText(messageText);

                        message.setX(image.getX());
                        message.setY(image.getY());

                        window.addView(message);

                        Animation animation = AnimationUtils.loadAnimation(MainActivity.super.getBaseContext(), R.anim.a);

                        animation.setAnimationListener(new Animation.AnimationListener() {

                            @Override
                            public void onAnimationStart(Animation animation) {
                            }

                            @Override
                            public void onAnimationRepeat(Animation animation) {
                            }

                            @Override
                            public void onAnimationEnd(Animation animation) {
                                window.post(() -> window.removeView(message));
                            }

                        });

                        message.startAnimation(animation);

                    });
                }

                for (int i = 0; i <= window.getChildCount(); i++) {

                    AnimatorSet animSetXY = new AnimatorSet();

                    animSetXY.playTogether(ObjectAnimator.ofFloat(window.getChildAt(i), "translationX", getRand(width)),
                            ObjectAnimator.ofFloat(window.getChildAt(i), "translationY", getRand(height)));

                    animSetXY.setDuration(3000).start();

                }

                handler.postDelayed(this, 3000);

            }

        });

    }

    int getRand(int max) {
        return 1 + new Random().nextInt(max - 2);
    }

}
