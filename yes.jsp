<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@ page import="比价.*" %>
<%@page import="java.io.BufferedReader"%>
<%@page import="java.io.File"%>
<%@page import="java.io.FileReader"%>
<%@page import="java.io.InputStreamReader"%>
<%@page import="java.io.FileInputStream"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
</head>
<body>
	<%  String s = String.valueOf(request.getAttribute("exerciseList"));
		int num = Integer.parseInt(s);
			 if(num==1){
				 String encoding="UTF-8";
				 File f = new File("D:\\测试.txt");
				 InputStreamReader read = new InputStreamReader (new FileInputStream(f),encoding);
				 BufferedReader bf = new BufferedReader(read);
				 String str;
				 while((str=bf.readLine())!=null)
				 {
				   String[] su=str.split(",");			 
    %>
             <p><%=su[0]%></p>
             <p><%=su[1]%></p>
             <p><%=su[2]%></p>
             <%}} %>
             <%if(s==null) { %>
             <%="no"%>
             <%} %>
</body>
</html>