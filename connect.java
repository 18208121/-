package 比价;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class connect {
	public String Return(String a) {
		String h = null;
		try {
		    String[] args = new String[] { "python", "D:\\Users\\86152\\PycharmProjects\\untitled\\商品价格.py", a };
		    Process proc = Runtime.getRuntime().exec(args);// 执行py文件
		    BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
		    String line = null;
		    while ((line = in.readLine()) != null) {
		       h = line;
		    }
		    in.close();
		    proc.waitFor();
		} catch (IOException e) {
		    e.printStackTrace();
		} catch (InterruptedException e) {
		    e.printStackTrace();
		}
		return h;
	}
	
}
