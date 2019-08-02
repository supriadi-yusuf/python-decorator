def bungkus_parameter( prm1, prm2, *prms):
	def bungkus(fungsi):
		def yg_dibungkus( a, b):
			return 'decorator : hasil eksekusi fungsi adalah {}'.format(str(fungsi( a, b)))

		print("decorator : fungsi yang di decorate adalah " + str(fungsi))
		return yg_dibungkus

	#print( "decorator : parameter decorator adalah {0:10s}, {1:10s}, {2:30s}".format( str(prm1), str(prm2), str(prms) ))
	#print( "decorator : parameter decorator adalah {0:s}, {1:s}, {2:s}".format( str(prm1), str(prm2), str(prms) ))
	print( "decorator : parameter decorator adalah {}, {}, {}".format( prm1, prm2, prms ))

	return bungkus

@bungkus_parameter('hello', 5000, 'tes', 123, 'tok tok tok')
def fungsi1(param1, param2):
	return 'ini fungsi 1, parameter fungsi : %s, %s' % ( str(param1), str(param2))

ans = input("apakah fungsi1 akan di-eksekusi?(y/t)" )
if(ans=='y'):
	print("jawaban anda : ", ans)
	#print( fungsi1)
	print( fungsi1( 'supriadi', 50))
	#print( fungsi1.__name__)
