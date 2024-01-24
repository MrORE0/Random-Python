num = int(input('Choose a number to be multiplied: '))
for nums in range (1,11,1):
    # print(f'{nums}*{num}={nums*num}')
    #print('%d * %d = %d' % (nums, num, num * nums))
    print('{0}*{1}={2}'.format(nums, num, num * nums))
