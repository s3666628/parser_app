
import parser_app.parser_app as my_parse

test_data = "udp4       0      0  192-168-1-126.tp.51855 a172-224-30-6.so.https  "

def test_parser():
    result = my_parse.parse(test_data)
    
    
    assert result[0][0]== "192-168-1-126"


# message = test_parser()

# print(message)


# # print((message[0][0]))

test_parser()