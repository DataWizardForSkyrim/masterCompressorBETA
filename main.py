import compressionmodpckg as cmp

evennumlist = [2, 4, 6, 8, 10, 12, 16]

mblockcunt = -1
compblockstr = ''
rawitemlist = []
compitemlist = []

# STILL NEED TO DO::
# multimodefndr NOT USED??? NEED 2 SEE HOW altmode IS FOUND W/O THAT FUNC
# NEED 2 TEST A DATA SET THAT GOES FROM xx.xx TO xxx.xx AND ETC

rfileprefix = "C:/Users/Ellio/Desktop/Compressor/historical_prices/"
afileprefix = "C:/Users/Ellio/Desktop/Compressor/compressed_prices/"
robject = open(rfileprefix + "test_prices.txt", "r")
aobject = open(afileprefix + "ctest_prices.txt", "a+")


def what2write(vara, varb, varc, vard):
	my_w_string = vara + '\n' + varb + '\n' + varc + '\n' + vard[0:len(vard) - 1] + '\n'
	return my_w_string


# noinspection PyUnboundLocalVariable
def startup(printbool, testbool):
	global mblockcunt
	global compblockstr
	global rawitemlist
	global compitemlist
	mblockcunt += 1
	compblockstr = cmp.num2str_comp(mblockcunt)
	if printbool:
		peeklist = cmp.peekfiletwo(robject, ' ', 100)
		print(peeklist)
		readamount = peeklist[1]
		print(readamount)

		cblock = robject.read(readamount)
		print(cblock)
		if peeklist[0]:
			#print('(~~~)')
			tblock = cmp.itemsep_errfixer(' ', cblock)
			cblock = tblock
			#print(cblock)
		itmlenhst = cmp.charfndr(' ', cblock, 100)
		print(itmlenhst)
		print(cmp.charerror)
		print(len(itmlenhst))
		citemhst = cmp.stringsep(cblock, itmlenhst)
		print(citemhst)
		decindhst = cmp.listcharfndr('.', citemhst)
		print(decindhst)
		runldechst = cmp.runlen_listcomp(decindhst)
		print(runldechst)
		cleanitmhst = cmp.listchar_remover(citemhst, '.')


		print(cleanitmhst)


		ssmodedict = cmp.multimode(cleanitmhst) # substring mode dictionary
		bytesaved = cmp.savedspace(ssmodedict)  # bytes saved from using mode (dictionary)
		# print(bytesaved)
		# print('\n')
		sortedbytes = cmp.dict_value_sort(bytesaved)    # sorted saved bytes (dictionary)
		print(sortedbytes)
		print('\n')
		keylist = cmp.dict_index(sortedbytes)
		keyendind = len(keylist) - 1
		mode = keylist[len(keylist) - 1]
		print(mode)
		print('\n')
		altmodedict = cmp.newdictfunc(keyendind, keylist, mode, cleanitmhst)
		# print(altmodedict)
		# print('\n')
		multimodebyte = cmp.savedspace(altmodedict)
		sortedmultimodebyte = cmp.dict_value_sort(multimodebyte)
		print(sortedmultimodebyte)
		print('\n')
		indmultimodebyte = cmp.dict_index(sortedmultimodebyte)
		altmode = indmultimodebyte[len(indmultimodebyte) - 1]
		print(altmode)
		print('\n')
		altmodebool = cmp.altmode_counter(altmode, cleanitmhst)
		print(altmodebool)
		if not altmodebool:
			altmode = '?'
		modecompitemblock = cmp.mcitemblock(cleanitmhst, mode, altmode, ['~', '|'])
		print(modecompitemblock)
		print('\n')
		padcomplist = cmp.string_padder('~', '|', '0', modecompitemblock)
		print(padcomplist)
		print('\n')
		padlist = cmp.mcomppad(padcomplist, ['~', '|'], evennumlist)  # THIS WORKS !!!!
		# print(padlist)
		reddlist = []
		templist = cmp.plist2str(padlist, '~|')


		compitm = ''
		for x in templist:  # might want to add this to init but not going to rn
			if x == ' ':
				reddlist.append(compitm)
				compitm = ''
			else:
				compitm += x
		print(reddlist)  # THIS WORKS !!!!
		print('\n')
		rancomplist = cmp.runlength_list(reddlist)
		print(rancomplist)

	#if printbool:
	#	# print(readamount)
	#	# print(len(itmlenhst))
	#	# print(decindhst)
	#	print(citemhst)
	#	print(cleanitmhst)
	#	# print(bytesaved)
	#	# print('\n')
	#	print(sortedbytes)
	#	print('\n')
	#	print(mode)
	#	print('\n')
	#	# print(altmodedict)
	#	# print('\n')
	#	print(sortedmultimodebyte)
	#	print('\n')
	#	print(altmode)
	#	print('\n')
	#	print(modecompitemblock)
	#	print('\n')
	#	print(padcomplist)
	#	print('\n')
	#	# print(padlist)
	#	print(reddlist)  # THIS WORKS !!!!
	#	print('\n')
	#	print(rancomplist)
	else:
		peeklist = cmp.peekfiletwo(robject, ' ', 100)
		readamount = peeklist[1]
		cblock = robject.read(readamount)
		if peeklist[0]:
			tblock = cmp.itemsep_errfixer(' ', cblock)
			cblock = tblock

		itmlenhst = cmp.charfndr(' ', cblock, 100)
		citemhst = cmp.stringsep(cblock, itmlenhst)
		decindhst = cmp.listcharfndr('.', citemhst)
		runldechst = cmp.runlen_listcomp(decindhst)
		cleanitmhst = cmp.listchar_remover(citemhst, '.')


		ssmodedict = cmp.multimode(cleanitmhst)
		bytesaved = cmp.savedspace(ssmodedict)
		sortedbytes = cmp.dict_value_sort(bytesaved)
		keylist = cmp.dict_index(sortedbytes)
		keyendind = len(keylist) - 1
		mode = keylist[len(keylist) - 1]
		altmodedict = cmp.newdictfunc(keyendind, keylist, mode, cleanitmhst)
		multimodebyte = cmp.savedspace(altmodedict)
		sortedmultimodebyte = cmp.dict_value_sort(multimodebyte)
		indmultimodebyte = cmp.dict_index(sortedmultimodebyte)
		altmode = indmultimodebyte[len(indmultimodebyte) - 1]
		altmodebool = cmp.altmode_counter(altmode, cleanitmhst)
		if not altmodebool:
			altmode = '?'


		modecompitemblock = cmp.mcitemblock(cleanitmhst, mode, altmode, ['~', '|'])
		padcomplist = cmp.string_padder('~', '|', '0', modecompitemblock)
		padlist = cmp.mcomppad(padcomplist, ['~', '|'], evennumlist)  # THIS WORKS !!!!
		reddlist = []
		templist = cmp.plist2str(padlist, '~|')

		compitm = ''
		for x in templist:  # might want to add this to init but not going to rn
			if x == ' ':
				reddlist.append(compitm)
				compitm = ''
			else:
				compitm += x
		rancomplist = cmp.runlength_list(reddlist)

	# TESTER!
	if testbool:
		controlstr = cmp.simple_list2str(citemhst, ' ')
		teststr = cmp.simple_list2str(rancomplist, ' ')

		xya = compblockstr = cmp.num2str_comp(mblockcunt)
		xyb = cmp.simple_list2str(runldechst, ' ')  # use a space in case decindhst has values similar to 2,3,3,2,3,3,3
		if altmodebool:
			xyc = mode + ' ' + altmode  # set up control if no altmode
		else:
			xyc = mode
		xyd = teststr
		# could do something where the modes are converted to two2onedict. eg; 300 = 3A, 0000 = AA
		finalresult = what2write(xya, xyb[:len(xyb) - 1], xyc, xyd)

		rawitemlist.append(controlstr)
		compitemlist.append(finalresult)

		print('\nTEST\n')
		print(controlstr)
		#print('*-*: ' + str(len(itmlenhst)))
		print()
		print(finalresult)
		print()
		print(len(controlstr))
		print()
		print(len(finalresult))


def master_controller(printb, testb, writeb):

	while not cmp.endofdocument:
		startup(printb, testb)
	mycntrlstr = ''
	mycompstr = ''
	for x1 in rawitemlist:
		for x2 in x1:
			mycntrlstr += x2
	for y1 in compitemlist:
		for y2 in y1:
			mycompstr += y2
	if writeb:
		aobject.write(mycompstr)
	if testb:
		print('\n' + mycntrlstr)
		print('\n' + mycompstr)

		print(len(mycntrlstr))
		print(len(mycompstr))
		print(1 - (len(mycompstr) / len(mycntrlstr)))
	robject.close()
	aobject.close()


master_controller(True, True, False)
