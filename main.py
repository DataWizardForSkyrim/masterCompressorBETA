import compressionmodpckg as cmp

evennumlist = [2, 4, 6, 8, 10, 12, 16]
modes = ['~', '|']      # might want to add an itemsep variable too

mblockcunt = -1
compblockstr = ''
rawitemlist = []
compitemlist = []

# STILL NEED TO DO::
# multimodefndr NOT USED??? NEED 2 SEE HOW altmode IS FOUND W/O THAT FUNC
# NEED 2 TEST A DATA SET THAT GOES FROM xx.xx TO xxx.xx AND ETC
# NEED TO DECIDE IF I ACTUALLY NEED THE BLOCK COUNTER

rfileprefix = "C:/Users/Ellio/Desktop/Compressor/historical_prices/"
afileprefix = "C:/Users/Ellio/Desktop/Compressor/compressed_prices/"
rfilesuffix = "test1_prices.txt"
hist_path = rfileprefix + rfilesuffix
robject = open(hist_path, "r")
aobject = open(afileprefix + "c" + rfilesuffix, "a+")
cblock = ''


testfuck = '30300'
altm_ind = testfuck.find('303')
print(altm_ind)


def what2write(vara, varb, varc, vard):
	my_w_string = vara + '\n' + varb + '\n' + varc + '\n' + vard[0:len(vard) - 1] + '\n'
	return my_w_string


# noinspection PyUnboundLocalVariable
def startup_c(printbool, testbool):
	global mblockcunt
	global compblockstr
	global rawitemlist
	global compitemlist
	global cblock
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
		#if controlstr == cblock:
		#	print(True)
		#print('*-*: ' + str(len(itmlenhst)))
		print()
		print(finalresult)
		print()
		print(len(controlstr))
		print()
		print(len(finalresult))


def master_controller(printb, testb, writeb):

	while not cmp.endofdocument:
		startup_c(printb, testb)
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
		#robject.seek(0)
		#tall = robject.read()
		#print(len(tall))
		print(len(mycompstr))
		print(1 - (len(mycompstr) / len(mycntrlstr)))
	robject.close()
	aobject.close()


master_controller(False, True, False)
print('\n\nDECOMP WORK::\n\n')
# ------~~~~~~------:::/// || DECOMPRESSOR || \\\:::------~~~~~~------ #

rfileprefix = "C:/Users/Ellio/Desktop/Compressor/compressed_prices/"
afileprefix = "C:/Users/Ellio/Desktop/Compressor/historical_prices/"
afilesuffix = "test1_prices.txt"
decomp_path = afileprefix + "d" + afilesuffix
# noinspection PyRedeclaration
robject = open(rfileprefix + "c" + afilesuffix, "r")
# noinspection PyRedeclaration
aobject = open(decomp_path, "a+")
endofrfile = False
rawcompdict = {}
quitingbool = False


def quitingfunc():
	global quitingbool
	quitingbool = True
	robject.close()
	aobject.close()


def rawitem_parse(rfileobj):
	global endofrfile
	ttimer = 0
	rawcompblock = {}
	while ttimer < 4:
		try:
			mystring = rfileobj.readline()
			#print(mystring)
			rawcompblock[str(ttimer)] = mystring[:len(mystring) - 1]
			ttimer += 1

	#for x in mystring:
	#	rawcompblock[str(ttimer)] = x[:len(x) - 1]
	#	ttimer += 1
		except IndexError:
			endofrfile = True
			break
		finally:
			if ttimer == 4:
				if not endofrfile:
					#print(rawcompblock)
					return rawcompblock


def cleanpadding(decomplist, padc, trailingb):
	tcleaned = []
	if not trailingb:
		for x in decomplist:
			if x[0] == padc:
				tcleaned.append(x[1:])
			else:
				tcleaned.append(x)
		return tcleaned
	else:
		for x in decomplist:
			trailchar = x[len(x) - 1]
			if trailchar == padc:
				tcleaned.append(x[:len(x) - 1])
			else:
				tcleaned.append(x)
		return tcleaned


def decompcontinue(printbo, writbo):
	if printbo:
		cdecindhst = rawcompdict['1']
		cmodes_str = rawcompdict['2']
		crawvalues = rawcompdict['3']
		print(rawcompdict)
		print('\n')

		citemlenhst = cmp.charfndr(' ', crawvalues, 99)

		tempnum = 0
		for tempclen in citemlenhst:
			tempnum += tempclen + 1
		tempcstr = crawvalues[tempnum:]
		#citemlenhst.append(len(tempcstr)) NOT WORKING FOR SOME REASON
		print(tempcstr)
		print(citemlenhst)
		#print(len(citemlenhst))
		citmhst = cmp.stringsep(crawvalues, citemlenhst)
		citmhst.append(tempcstr)
		print(citmhst)
		#print(len(citmhst))
		onemode = True
		try:
			cspaceind = cmodes_str.index(' ')
			cmodelist = [cmodes_str[:cspaceind], cmodes_str[cspaceind + 1:]]
			cmode = cmodelist[0]
			caltmode = cmodelist[1]
			onemode = False
		except Exception:
			cmode = cmodes_str
		#print(cmode)
		tdecompstr = ''

		tdecomplist = []
		for citem in citmhst:
			tdc = ''
			tdecompbool = True
			for cchar in citem:
				#print(cchar)
				crunl = cchar.isnumeric()
				#print(crunl)
				if crunl:
					if int(cchar) in range(1, 99):
						comprun = int(cchar)
						while comprun > -1:
							tdecomplist.append(tdc)
							tdecompstr += tdc + ' '
							comprun -= 1
							tdecompbool = False
						break
				else:
					pass
				if onemode:
					if cchar == modes[0]:
						tdc += cmode
					else:
						tdc += cmp.inverse2to1[cchar]
				else:
					if cchar == modes[0]:
						tdc += cmode
					elif cchar == modes[1]:
						# noinspection PyUnboundLocalVariable
						tdc += caltmode
					else:
						tdc += cmp.inverse2to1[cchar]
			if tdecompbool:
				tdecomplist.append(tdc)
				tdecompstr += tdc + ' '

		#print(tdecompstr)
		print(tdecomplist)


		cleandecomplist = cleanpadding(tdecomplist, '0', False)    # will set up control here for values like '0.14725'
		clncompl = cleanpadding(cleandecomplist, '0', True)
		cleandecomplist = clncompl

		decompdecstr = ''
		decompdeclst = []
		if cdecindhst[1:2] == '~':
			for ci in cleandecomplist:
				cdind = int(cdecindhst[0:1])
				cbstr = ci[:cdind]
				castr = ci[cdind:]
				cdres = cbstr + '.' + castr
				decompdecstr += cdres + ' '
				decompdeclst.append(cdres)

		print(decompdeclst)
		print(len(decompdecstr))
	else:
		cdecindhst = rawcompdict['1']
		cmodes_str = rawcompdict['2']
		crawvalues = rawcompdict['3']

		citemlenhst = cmp.charfndr(' ', crawvalues, 99)

		tempnum = 0
		for tempclen in citemlenhst:
			tempnum += tempclen + 1
		tempcstr = crawvalues[tempnum:]
		# citemlenhst.append(len(tempcstr)) NOT WORKING FOR SOME REASON

		citmhst = cmp.stringsep(crawvalues, citemlenhst)
		citmhst.append(tempcstr)

		onemode = True
		try:
			cspaceind = cmodes_str.index(' ')
			cmodelist = [cmodes_str[:cspaceind], cmodes_str[cspaceind + 1:]]
			cmode = cmodelist[0]
			caltmode = cmodelist[1]
			onemode = False
		except Exception:
			cmode = cmodes_str
		# print(cmode)
		tdecompstr = ''

		tdecomplist = []
		for citem in citmhst:
			tdc = ''
			tdecompbool = True
			for cchar in citem:
				# print(cchar)
				crunl = cchar.isnumeric()
				# print(crunl)
				if crunl:
					if int(cchar) in range(1, 99):
						comprun = int(cchar)
						while comprun > -1:
							tdecomplist.append(tdc)
							tdecompstr += tdc + ' '
							comprun -= 1
							tdecompbool = False
						break
				else:
					pass
				if onemode:
					if cchar == modes[0]:
						tdc += cmode
					else:
						tdc += cmp.inverse2to1[cchar]
				else:
					if cchar == modes[0]:
						tdc += cmode
					elif cchar == modes[1]:
						# noinspection PyUnboundLocalVariable
						tdc += caltmode
					else:
						tdc += cmp.inverse2to1[cchar]
			if tdecompbool:
				tdecomplist.append(tdc)
				tdecompstr += tdc + ' '

		cleandecomplist = cleanpadding(tdecomplist, '0', False)    # will set up control here for values like '0.14725'
		clncompl = cleanpadding(cleandecomplist, '0', True)
		cleandecomplist = clncompl

		decompdecstr = ''
		decompdeclst = []
		if cdecindhst[1:2] == '~':
			for ci in cleandecomplist:
				cdind = int(cdecindhst[0:1])
				cbstr = ci[:cdind]
				castr = ci[cdind:]
				cdres = cbstr + '.' + castr
				decompdecstr += cdres + ' '
				decompdeclst.append(cdres)
	if writbo:
		aobject.write(decompdecstr)
	else:
		print(decompdecstr)


def startup_d(pbo, wbo):
	global rawcompdict
	rawcompdict = rawitem_parse(robject)
	blockchar = rawcompdict['0']    # might not need block timer
	if blockchar != '':
		decompcontinue(pbo, wbo)
	else:
		quitingfunc()


while not quitingbool:
	startup_d(True, False)


def fidelity_test(histfile, decompfile):
	a = open(histfile, 'r')
	b = open(decompfile, 'r')
	x = a.read()
	y = b.read()
	if x == y:
		return True
	else:
		return [x, y]

fidtest = fidelity_test(hist_path, decomp_path)

# noinspection PySimplifyBooleanCheck
def fdetail_test():
	if fidtest != True:     # This pops up when double spacing occurs in raw file
		tnumcnt = 0
		tcheck1 = fidtest[0]
		tcheck2 = fidtest[1]
		for traw in tcheck1:
			tcheck = tcheck2[tnumcnt:tnumcnt + 1]
			if traw == tcheck:
				pass
			else:
				print(traw + ' - ' + tcheck + ' - ' + str(tnumcnt) + ' ---kkk')
	# 3 - 0 - 2109 ---kkk
	# 3 - 0 - 2123 ---kkk
			tnumcnt += 1

		print(tcheck1[26870:26885] + '| - |' + tcheck2[26870:26885])
		#print(tcheck1[2119:2128] + '| - |' + tcheck2[2119:2128])
		print(str(len(tcheck1)) + ' ' + str(len(tcheck2)))


if fidtest:
	print(fidtest)
else:
	#fdetail_test()
	pass



#for tempf in cmp.two2onedict.keys():
#	print("'" + cmp.two2onedict[tempf] + "': '" + tempf + "', ")
