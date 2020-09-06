<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<!DOCTYPE html>
<%
	String webroot = request.getContextPath();
%>
<html>
	<head>
		<meta charset="utf-8" />
		<title>首页</title>
		<style>
			/*第一部分：Logo部分*/
			.header {
				width: 100%;
			}

			.header div {
				/*左浮动*/
				float: left;
				width: 33.3%;
				height: 75px;
				/*行高*/
				line-height: 50px;
			}

			/*a标签*/
			/*控制Logo部分的a标签*/
			.header a {
				color: #000;
				/*颜色*/
			}

			a {
				font-size: 12px;
				/*字体*/
				padding: 10px;
				/*控制内边距*/
				text-decoration: none;
				/*去掉超链接的下划线*/
			}

			/*第二部分：导航栏部分*/
			/*清除浮动*/
			.clear {
				clear: both;
			}

			.menu {
				width: 100%;
				background-color: #000;
				height: 50px;
				padding-top: 1px;
			}

			.menu ul li {
				/*去掉标记*/
				list-style-type: none;
				/*元素设为同一行*/
				display: inline;
			}

			.menu a {
				color: #FFF;
			}

			/*第三部分：轮播图*/
			* {
				margin: 0;
				padding: 0;
				list-style: none;
			}

			#img1 {
				width: 100%;
				border: 1px solid #000;
				height: 400px;
				margin: 30px auto;
				position: relative;
				overflow: hidden;
			}

			#img1 ul {
				position: absolute;
				left: 0;
				top: 0;
			}

			#img1 ul li {
				width: 800px;
				height: 400px;
				float: left;
				padding: 5px;
			}

			/*第四部分+第六部分：最新+热门商品*/
			.hot {
				height: 50px;
				padding-top: 10px;
			}

			/*左边大图*/
			.left {
				float: left;
				width: 16%;
				height: 500px;
			}

			.right {
				float: left;
				width: 84%;
				text-align: center;
				height: 500px;
			}

			.middle {
				float: left;
				width: 50%;
				height: 250px;
			}

			.item {
				float: left;
				width: 16.6%;
				height: 250px;
			}

			/*第五+七部分:广告图片+正品保证*/
			.adv {
				width: 100%;
			}

			/*第八部分:页脚部分*/
			.foot {
				width: 100%;
			}

			.foot p {
				text-align: center;
			}
		</style>
		<script>
			window.onload = function() {
				var oBox = document.getElementById('img1');
				var oUl = oBox.children[0];
				var aLi = oUl.children;

				//复制一份内容 ，制作出无缝的效果   
				oUl.innerHTML += oUl.innerHTML;
				oUl.style.width = aLi.length * aLi[0].offsetWidth + 'px';

				setInterval(function() { //开定时器，这样就可以自己切换，无需人工干预。 
					var l = oUl.offsetLeft - 2; //图片切换，就是移动距离(速度)
					if (l <= -oUl.offsetWidth / 2) {
						l = 0;
					}
					oUl.style.left = l + 'px';
				}, 30);
			};
		</script>
	</head>
	<body>
		<div>
			<!--第一部分：Logo部分-->
			<div class="header">
				<div id="d1-1"><img src="imge/loge.jpg" height="70px" /></div>
				<div id="d1-2"><img src="imge/header.png" /></div>
				<div id="d1-3" align="center">
					<a href="Enter.html">登录</a>
					<a href="login.html">注册</a>
				</div>
			</div>
			<!--第二部分：导航栏部分-->
			<!--清除浮动-->
			<div class="clear"></div>
			
			<div class="change">
				<form action="listcxercise" method="post">
				<input type="text" name="a" id="a" value="" />
				<input type="submit" name="搜索" id="c" value="搜索" />
				</form>
			<div>
				
			</div>
			
			<div class="menu">
				<ul>
					<li><a href="home.html">首页</a></li>
					<li><a href="home.html">手机数码</a></li>
					<li><a href="home.html">电脑办公</a></li>
					<li><a href="home.html">鞋靴箱包</a></li>
					<li><a href="home.html">户外</a></li>
				</ul>
			</div>
			<!--第三部分：轮播图部分-->
			<div id="img1" align="center">
				<ul>
					<li><img src="imge/1.jpg"></li>
					<li><img src="imge/2.jpg"></li>
					<li><img src="imge/3.jpg"></li>
					<li><img src="imge/4.jpg"></li>
				</ul>
			</div>
			<!--第四部分：最新商品部分-->
			<div>
				<div class="hot">
					<h3 style="display: inline;">最新商品</h3>
					<img src="imge/title1.png" />
				</div>
				<!--左边大图+右边商品-->
				<!--左边大图-->
				<div class="left">
					<img src="imge/big01.jpg" width="95%" />
				</div>
				<!--右边商品-->
				<div class="right">
					<div class="middle">
						<img src="imge/middle01.jpg" width="95%" height="240px" />
					</div>
					<div class="item">
						<img src="imge/small01.jpg" />
						<p><a href="http://www.example.com">豆浆机</a></p>
						<p>
							<font color="red">$298</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/small02.jpg" />
						<p><a href="http://www.example.com">电脑</a></p>
						<p>
							<font color="red">$6998</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/small03.jpg" />
						<p><a href="http://www.example.com">洗衣机</a></p>
						<p>
							<font color="red">$398</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/small04.jpg" />
						<p><a href="http://www.example.com">热水器</a></p>
						<p>
							<font color="red">$298</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/small05.jpg" />
						<p><a href="http://www.example.com">微波炉</a></p>
						<p>
							<font color="red">$998</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/small06.jpg" />
						<p><a href="http://www.example.com">电暖气</a></p>
						<p>
							<font color="red">$1998</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/small07.jpg" />
						<p><a href="http://www.example.com">照相机</a></p>
						<p>
							<font color="red">$998</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/small08.jpg" />
						<p><a href="http://www.example.com">吹风机</a></p>
						<p>
							<font color="red">$598</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/small09.jpg" />
						<p><a href="http://www.example.com">电视机</a></p>
						<p>
							<font color="red">$398</font>
						</p>
					</div>
				</div>
			</div>
			<!--第五部分:广告图片-->
			<div class="adv">
				<img src="imge/ad.jpg" width="100%" />
			</div>
			<!--第六部分：热门商品部分-->
			<div>
				<div class="hot">
					<h3 style="display: inline;">热门商品</h3>
					<img src="imge/title1.png" />
				</div>
				<!--左边大图+右边商品-->
				<!--左边大图-->
				<div class="left">
					<img src="imge/rm.png" width="95%" />
				</div>
				<!--右边商品-->
				<div class="right">
					<div class="middle">
						<img src="imge/new_right.jpg" width="95%" height="240px" />
					</div>
					<div class="item">
						<img src="imge/c_005.jpg" />
						<p><a href="http://www.example.com">小米</a></p>
						<p>
							<font color="red">$1998</font>
					</div>
					<div class="item">
						<img src="imge/c_006.jpg" />
						<p><a href="http://www.example.com">vivo</a></p>
						<p>
							<font color="red">$1998</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/c_007.jpg" />
						<p><a href="http://www.example.com">oppo</a></p>
						<p>
							<font color="red">$1998</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/c_008.jpg" />
						<p><a href="detail.html">华为</a></p>
						<p>
							<font color="red">$1998</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/c_009.jpg" />
						<p><a href="http://www.example.com">苹果</a></p>
						<p>
							<font color="red">$1998</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/c_010.jpg" />
						<p><a href="http://www.example.com">魅族</a></p>
						<p>
							<font color="red">$1998</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/c_011.jpg" />
						<p><a href="http://www.example.com">三星</a></p>
						<p>
							<font color="red">$1998</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/c_012.jpg" />
						<p><a href="http://www.example.com">努比亚</a></p>
						<p>
							<font color="red">$1998</font>
						</p>
					</div>
					<div class="item">
						<img src="imge/c_013.jpg" />
						<p><a href="http://www.example.com">诺基亚</a></p>
						<p>
							<font color="red">$1998</font>
						</p>
					</div>
				</div>
			</div>
			<!--第七部分：正品保证-->
			<div class="adv">
				<img src="imge/footer.jpg" width="100%" />
			</div>
			<!--第八部分:页脚部分-->
			<div class="foot">
				<p>
					<a href="http://www.swu.edu.cn/">关于我们</a>
					<a href="http://www.swu.edu.cn/">联系我们</a>
					<a href="http://www.swu.edu.cn/">投诉建议</a>
				</p>
				<p>
					给力商城
				</p>
			</div>
		</div>
	</body>
</html>
