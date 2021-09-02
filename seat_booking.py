import time

class SeatBooking:
  # 展示所有座位的预订信息
  def check_bookings(self, seats):
    print("正在为您查询该场次电影的预订状态...")
    time.sleep(0.7)
    print('从上到下为 1～6 排，从左至右为 1～8 座')
    print("======================")
    for row in seats:
      time.sleep(0.1)
      print('  '.join(row))
    print("======================")
    time.sleep(0.7)
  
  # 获取符合要求的行索引
  def get_row(self):
    input_row = input("预订第几排的座位呢？请输入 1～6 之间的数字")
    valid_row = [str(i + 1) for i in range(6)]

    while input_row not in valid_row:
      input_row = input('没有按要求输入哦，请输入 1～6 之间的数字')

    row = int(input_row) - 1
    return row
  
  # 获取符合要求的列索引
  def get_col(self):
    input_column = input('预订这一排的第几座呢？请输入 1～8 之间的数字')
    valid_column = [str(i + 1) for i in range(8)]

    while input_column not in valid_column:
      input_column = input('没有按要求输入哦，请输入 1～8 之间的数字')

    column = int(input_column) - 1
    return column

  # 预订指定座位
  def book_seat(self, seats):
    while True:
      row = self.get_row()
      column = self.get_col()
      # 指定座位没有被预订
      if seats[row][column] == '○':
        print("正在为您预订指定座位...")
        time.sleep(0.7)
        seats[row][column] = '●'
        print("预订成功！座位号：{}排{}座".format(row + 1, column + 1))
        break  # 结束循环，退出选座
      # 指定座位已经被预订了
      else:
        print("这个座位已经被预订了哦，试试别的吧")
        time.sleep(0.7)
