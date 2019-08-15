---
title: 几个C++数字转字符串（int转string）函数与其复杂度比较
tags:
  - C++
  - C++类型转换
  - int转string
  - itoa
  - 数字转字符串
  - 算法
id: 256
categories:
  - C++ / Visual C++
  - 算法、
date: '2015-12-29T13:06:53.000Z'
---

# 几个C++数字转字符串（int转string）函数与其复杂度比较

前几天在做一道ACM题的时候，这道题要求我们对输入的2个数字逆序相加，再将它们的和逆序输出。当时我直接调用了itoa函数进行数字到字符串的转换，再用我之前的AddNum函数进行加法运算。结果上传到BNUOJ上后，居然编译错误。提示：

```text
error: 'itoa' was not declared in this scope
```

 后来无奈只有自己实现这个函数。数字转字符串之前在C语言课上我写过一个。不过，这次我想到了一个特别的方法。下面来详细说说这几个方法吧。 \* \* \*   \#\# 方法一 首先，先来谈谈我最早在C语言上的方法： 之前我都这样做，每次用这个数去除以小于它的10^n数，再利用C/C++ int类型取整的特性，来得到要转换数字的每个数位。 比如，对于4567这个数字，我先用1000去除，得到第一个数位4；再用100除它，得到的数字X减去之前得到的数字乘以10，就得到第二个数位5；同理，再继续将4567除以10，得到数再减去之前得到的中间数乘以10，就得到第三个数位6，再用同样的方法得到第4个数位。 最后，整个算法是这个样子的：

```text
void itoc(long n,char * num)
{
    int len=0, p=n;
    while(p/=10)
    {
        len++;
    }
    len++;
    for(p=0;p<len;p++)
    {
        int x=1;
        for(int t=p+1;t<len;t++)
        {
            x*=10;
        }
        num[p] = n/x + '0';
        n -=( num[p] - '0' ) * x;
    }
    num[len] = '\0';
}
```

   \#\# 方法二 其次，我们来谈谈这次我的方法： 原理很简单，我们不做除法，不是完全不做，我们一直做减法就行。比如还是对于4567这个数字，首先，我们知道的是：4567和10求余肯定不为0。所以我们就一直让4567减1，直到4567和10求余余数为0就停止。然后我们再将现在的这个数字，也就是4560除10，得到456，再用同样的方法，依次递减1，直到450为止，从而得到第二个数位6，依次这样做下去，我们就可以得到第3，第4个数位了。 最后，整个算法是这个样子的：

```text
inline string inttostr(int num)
{
    int buf=num,x=0;
    string snum="";
    while(1)
    {
        //if(buf==1)
        if(buf<10)
        {
            char ch=buf+'0';
            snum+=ch;
            break;
        }
        else if(buf%10)
        {
            buf--;
            x++;
        }
        else if(!(buf%10) && buf !=0)
        {
            char ch=x+'0';
            snum+=ch;
            buf /= 10;
            x=0;
        }
    }

    return snum;
}
```

## 系统的方法

再看看系统，不对，是某某库的itoa方法：

[![itoa\_1](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/12/itoa_1.jpg)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/12/itoa_1.jpg)

stdlib.h库里函数的方法用了和方法一原理上相同的方法，只不过，好吧，他这个可以判断正负。写得好简洁。

几种方法的效率分析：

我们用这三个算法进行50000次int到str的转换，结果如下：

[![inttostr](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/12/inttostr.png)](https://raw.githubusercontent.com/ankanch/blog/master/images/wp-content/uploads/2015/12/inttostr.png)

什么鬼这是，我的新方法居然慢了这么多，，，，悲剧了。

可以看到，传统方法和标准库里面的方法在速度上没太大的区别。新方法呢，，，的确，慢了好多。



{% include post_footer.md %}