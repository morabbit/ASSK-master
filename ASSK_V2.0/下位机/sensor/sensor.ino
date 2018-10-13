int powerPin = 7;//传感器供电针脚
int coefficient = 1;//电压与酒精浓度的系数
char concentration[25];//上报的酒精浓度

void setup() 
{
  Serial.begin(9600);//初始化串口波特率
  //shake();//与上位机通讯握手
  pinMode(powerPin, OUTPUT);//打开供电
  digitalWrite(powerPin, HIGH);//开始供电
}

void loop() 
{
  if(volts > 500)//防止电压过高
  {
    digitalWrite(powerPin, LOW);//断电
    delay(5000);//延迟5秒，让传感器冷却一下
  }
  
  if(volts < 0)//如果数据错误，清洗
  {
    continue;//跳过
  }
  
  int volts;//读取的酒精数值
  volts = analogRead(0);//从arduino的A0口获取传感器的电压数值
  delay(10);//等待10ms，让ADC数模转换电路完成处理工作：
  int temp = volts * coefficient;//计算浓度
  itoa(temp, concentration+"\n", 10);//将整型转为字符串
  Serial.println(concentration, DEC);//十进制输出
}

void shake()
{
  while(!Serial) // 等待串口建立完成,只有当使用本地USB口时有用
  {
    void serial_init();//串口初始化
  } 
  while(Serial.available() <= 0) //初始化的串口没有数据
  {
    Serial.print("I am Arduino!\n");//发送消息
    delay(10);//延迟等待上位机回报数据
  }
  while(Serial.available() > 0)//如果串口可获得了数据
  {
    int upperCall = Serial.read();//读取上位机返回的消息
    if(upperCall = 1)//如果上位机返回数字1，表示连接已经建立
    {
      break;//退出循环
    }
  }
}

