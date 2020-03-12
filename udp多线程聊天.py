# @ Time    : 2020/2/7 15:37
# @ Author  : Emily
'''
1 创建套接字
2 绑定本地信息
3 获取对方IP和端口
4 发送、接收数据
5 创建两个线程，去执行功能
'''
import socket
import threading


"""接收数据"""
def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


"""发送数据"""
def send_msg(udp_socket, dest_ip, dest_port):
    while True:
        send_data = input("输入要发送的数据：")
        udp_socket.sendto(send_data.encode('gbk'), (dest_ip, dest_port))


def main():
    """udp聊天器收发"""
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定
    udp_socket.bind(("", 7788))

    # 获取对方的IP和端口 dest_ip和dest_port是网络设置里面的本地主机地址和本地主机端口
    # dest_ip = input("请输入对方的IP:")
    dest_ip = "192.168.16.1"
    # dest_port = int(input("请输入对方的port："))   #这里需要对数据类型强转成int
    dest_port = 7890

    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg,args=(udp_socket, dest_ip, dest_port))

    t_recv.start()
    t_send.start()


if __name__ == '__main__':
    main()