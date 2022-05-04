#consider below dictionary and print necessary fields as shown below
#     ex:     input:
# 				{'stream_group01': {'stream_group01-EndpointSet-1 - Flow Group 0001': {'Tx Frames': '219874', 'Rx Frames': '1978866', 'Loss %': '', 'Frames Delta': '1758992', 'Tx Frame Rate': '1000.000', 'Rx Frame Rate': '9000.000'}}, 'stream_group02': {'stream_group02-EndpointSet-1 - Flow Group 0001': {'Tx Frames': '209257', 'Rx Frames': '1255542', 'Loss %': '', 'Frames Delta': '1046285', 'Tx Frame Rate': '1000.000', 'Rx Frame Rate': '6000.000'}}}
				
# 			output:
# 				Transmitted rate is 1000.00 and Received rate is 9000.00 on stream_group01-EndpointSet-1 - Flow Group 0001 of stream_group01
# 				Transmitted rate is 1000.00 and Received rate is 9000.00 on stream_group01-EndpointSet-1 - Flow Group 0001 of stream_group02


data = {'stream_group01': {'stream_group01-EndpointSet-1 - Flow Group 0001': {'Tx Frames': '219874', 'Rx Frames': '1978866', 'Loss %': '', 'Frames Delta': '1758992', 'Tx Frame Rate': '1000.000', 'Rx Frame Rate': '9000.000'}}, 'stream_group02': {'stream_group02-EndpointSet-1 - Flow Group 0001': {'Tx Frames': '209257', 'Rx Frames': '1255542', 'Loss %': '', 'Frames Delta': '1046285', 'Tx Frame Rate': '1000.000', 'Rx Frame Rate': '6000.000'}}}

for key, value in data.items():
    dic = data[key]
    for k, v in dic.items():
        d = dic[k]
        print("Transmitted rate is  ",d['Tx Frame Rate'],"and Received rate is ",d['Rx Frame Rate'],"on",k," of ",key)

    
