package net.lihulab;

public class wangdachui {
    public static void main(String[] args) {

    }

    private String wangda(String sentence) {
        char[] sen = sentence.toCharArray();
        for (int i = 0; i < sen.length; i++) {
            char a1 = sen[i];
            int cnt = 1;
            for (int j = i+1; j < sen.length; j++) {
                char a2 = sen[j];
                if (a1 == a2) {
                    cnt++;
                }
            }
            if (cnt > 2) {
                for (int k = i+1; k <= i+cnt; k++)
                    sen[i] = 0;
                i += cnt + 1;
            }
        }


    }
}
