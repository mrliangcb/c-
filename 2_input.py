手指或者鼠标事件

1.Input.GetMouseButtonDown()用法
每一帧中鼠键是否被按下
因为这个值在每一帧中都会被重置
必须在update（）方法中调用该方法。 
鼠键按下并释放时才会返回true

ButtonUp()相反

MouseButton()鼠键按下并释放时才会返回true

括号里面可以甜0（检测左击） 1（右击） 2（）  

用法if(Input.GetMouseButton(0))   左击按下且释放

2. if (Input.touchCount > 0) 手指触碰数量 此帧

3.Input.GetTouch(0).phase  == TouchPhase.Began;// 第一只手指刚触摸到屏幕的时候
用法if(按下的手指>0 && 而且刚按下的状态)

4.Input.GetTouch(0).phase  == TouchPhase.Moved;// 手指在屏幕上移动

5.Input.GetTouch(0).phase  == TouchPhase.Stationary;
// 手指触摸屏幕，但并未移动

6.Input.GetTouch(0).phase  == TouchPhase.Ended;
// 手指从屏幕上移开，这是一个触控的最后状态

7.Input.GetTouch(0).phase  == TouchPhase.Canceled;
/ 系统取消追踪触控。这常发生在用户把屏幕放到脸上或者同时触控超过了5根手指，同样也是触控的最后一个状态

8.保存触摸点
Touch touch = Input.GetTouch(0);

