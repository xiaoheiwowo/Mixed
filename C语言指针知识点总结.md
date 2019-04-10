# C语言指针知识点总结



## 指针引用数组

~~~c
int array[8];	// 数组名 array 的值为array[0]的地址
int *p;		    // 声明指针
p = array; 		// 或者 p = &array[0]
~~~





## 指向函数的指针

~~~c
int fun(int x);  // 声明函数
int (*p)(int x); // 声明指针，类型和参数要和对应函数一致
p = fun;         // 让指针指向函数
*p(3);			// 使用指针调用函数
~~~







## 返回指针值的函数

~~~ c
int *a()｛
	int *p;
	int a;
	a = 3;
	p = &a;
	return p;
｝

// 调用
int *m;
m = a();
~~~



> 引用部分

![1526892937518](C:\Users\LIUPEN~1\AppData\Local\Temp\1526892937518.png)

![1526894209308](C:\Users\LIUPEN~1\AppData\Local\Temp\1526894209308.png)





#### 参考

- C语言程序设计（第四版）唐浩强著 

  ​

