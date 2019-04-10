# NoteBook
##  widget
###  QLabel 与 QEditLine 关联
    lb1 = QLabel('$DownLoad',self)
    ed2 = QLineEdit(self)
    lb1.setBuddy(ed2)

###  消息提示框QMessageDialog
    def openmsg(self):
        reply = QMessageBox.information(self,'标题','消息正文',QMessageBox.Yes
        |QMessageBox.No,QMessageBox.Yes)
        print(reply)
### 输入框 QInputDialog
    def openinput(self):
        text, ok = QInputDialog.getText(self, 'tset input', 'input', )
        if ok:
            self.LineEdit.setText(str(text))
### 文件对话框 QFileDialog
    def getfile(self):
        fname , _ = QFileDialog.getOpenFileName(self, 'open', 'd:\\', 'Image files (*.jpg *.gif)')
        self.label.setPixmap(QPixmap(fname))

###  无边框（最大化：PyQt5快速开发与实战P377）
    self.setWindowFlags(Qt.FramelessWindowHint)

###  绘制文字
    def paintEvent(self,event):
        painter = QPainter(self)
        painter.begin(self)
        self.drawText(event,painter)
        painter.end()
    
    def drawText(self,event,gp):
        gp.setPen(QColor(168,34,3))
        gp.setFont(QFont('SimSun',90))
        gp.drawText(event.rect(),Qt.AlignCenter,self.text) #event.rect()是当前窗口的尺寸和位置

###  设置pen 导入图片 画圆角矩形
    qp.setPen(QPen(Qt.blue, 2, Qt.DashDotLine))
    qp.drawImage(QRect(160,30,300,300),QImage('../qt.png'))
    qp.drawRoundedRect(100,30,50,50,10,10)

###  重绘
    update()

###  日历
    self.cal.clicked[QtCore.QDate].connect(self.showDate)
    self.lb.setText(self.date.toString('yyyy-MM-dd dddd'))
###  常用设置
    objectName 控件对象名称 例：quitButton= QtWidgets.QPushButton() 等号前面的那个名字
    geometry 相对坐标系
    sizePolicy 控件大小策略
    minimumSize最小宽度、高度
    maximumSize最大宽度、高度  如果想让窗体或控件固定大小，可以将mini和max这两个属性设置成一样的数值
    font 字体
    cursor 光标
    windowTitle 窗体标题
    windowsIcon / icon 窗体图标/控件图标
    iconSize 图标大小
    toolTip 提示信息
    statusTip 任务栏提示信息
    text 控件文字
    shortcut 快捷键
### 转换

    int(x [,base ])         将x转换为一个整数    
    long(x [,base ])        将x转换为一个长整数    
    float(x )               将x转换到一个浮点数    
    complex(real [,imag ])  创建一个复数    
    str(x )                 将对象 x 转换为字符串    
    repr(x )                将对象 x 转换为表达式字符串    
    eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象    
    tuple(s )               将序列 s 转换为一个元组    
    list(s )                将序列 s 转换为一个列表    
    chr(x )                 将一个整数转换为一个字符    
    unichr(x )              将一个整数转换为Unicode字符    
    ord(x )                 将一个字符转换为它的整数值    
    hex(x )                 将一个整数转换为一个十六进制字符串    
    oct(x )                 将一个整数转换为一个八进制字符串    

软件
卸载， geek uninstall

### PCA9535 中断

    中断是由输入模式中端口输入的任何上升或下降边缘产生的。一段时间后，该信号是有效的，在。当端口上的数据更改为原始设置时，就可以重置中断电路，从生成中断的端口读取数据。复位发生在读取模式的确认（ACK）或不确认（NACK）点后SCL信号上升沿中断ACK或NACK时钟脉冲期间发生的丢失可以（或很短）由于复位中断在这个脉冲。复位后的I/O的每一个变化都被检测到，并以int形式发送给另一个设备，不影响中断电路，而配置为输出的PIN不能导致中断。如果输入引脚的状态与输入端口寄存器的内容不匹配，则将输出的I/O更改为输入可能会导致假中断。由于每个8位端口是独立读取的，端口0引起的中断没有被端口1的读取清除，反之亦然。INT输出有一个开漏结构，需要上拉电阻到VCC。

### 修改树莓派主机名hostname

    临时修改主机名：sudo hostname 新的主机名
    永久修改主机名：
        主机名存储在两个地方，两个地方都有修改
        sudo nano /etc/hostname，将原本的名称改为新的主机名
        sudo nano /etc/hosts，同样将原本的名称改为新的主机名
        重启

### 树莓派网络配置

    在dhcpcd.conf后添加以下内容：
        interface eth0
        static ip_address=192.168.1.122/24
        static routers=192.168.1.1
        static domain_name_servers=8.8.8.8 114.114.114.114
    保存后重启树莓派

### 7寸触摸屏

    max_usb_current=1
    hdmi_group=2
    hdmi_mode=87
    hdmi_cvt 1024 600 60 6 0 0 0
    hdmi_drive=1

### 树莓派串口配置

    禁用蓝牙：dtoverlay=pi3-disable-bt
    raspi-config中关闭串口调试，启用串口

### 服务器IP变化后
    ssh-keygen -R (SERVER IP)