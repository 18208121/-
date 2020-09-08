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
<title>商品展示</title>
<title>Insert title here</title>
</head>
<body>
	 <ul>
	<%  String[] s = (String[])request.getAttribute("exerciseList");
		int num = Integer.parseInt(s[0]);
			 if(num==1){
				 String encoding="UTF-8";
				 File f = new File("E:\\python数据\\商品\\"+s[1]+".txt");
				 InputStreamReader read = new InputStreamReader (new FileInputStream(f),encoding);
				 BufferedReader bf = new BufferedReader(read);
				 String str;
				 while((str=bf.readLine())!=null)
				 {
				   String[] su=str.split(",");			 
    %>
             <li>
             <p><%=su[0]%></p>
             <p><%=su[1]%></p>
             <div>
             <a target="_blank" title=<%=su[0] %> href=<%=su[3] %> onclick="searchlog(1, '62541363390','26','2','','flagsClk=2097166');">
             			<img width="220" height="220" data-img="1" src=<%=su[2]%> data-lazy-img="done" source-data-lazy-img="">	
             			</a></p>
             </div>
             <p>来源<%=su[4] %></p>
             </li>
             <%}} %>
              </ul>
             <%if(num==2) { %>
             <%="no"%>
             <%} %>
</body>
</html>