# mastercompressormods.py
# COLLECTION OF ALL FINISHED MODULES NEEDED FOR masterCompressor.py
# WILL STILL KEEP MODULES IN SEPARATE FILES FOR EZ USE WITH OTHER PROGRAMS HOWEVER, I MIGHT END UP MAKING A DIFFERENT -
# - MOD PACKAGE FILE FOR THE MAIN MODS I USE. THEN JUST USE from modmain.py import modname FOR FUTURE PROJECTS.
from itertools import combinations

endofdocument = False
charerror = False

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # --- # REVISED # --- # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


# 3/19/21   # returns the amount of chars needed 2b read n order 2 get set quantity of itemsep instances & itemcharerr
# noinspection PyGlobalUndefined,PyUnboundLocalVariable
def peekfiletwo(fnametwo, itemsep, itemcnt):
	global ramount
	global endofdocument
	global charerror
	referind = fnametwo.tell()
	laststr = ''
	charerror = False
	try:
		itemsepcnt = 0
		ramount = 0
		while itemsepcnt != itemcnt:
			try:
				tstring = fnametwo.read(1)
				if tstring == itemsep:
					if laststr == itemsep:
						itemsepcnt -= 1
					else:
						itemsepcnt += 1
						charerror = True
						pass
				elif tstring == '':
					endofdocument = True
					return ramount
				else:
					pass
			finally:
				laststr = tstring
				ramount += 1
	except Exception:# as peekfiletwoErr:
		#print(peekfiletwoErr)
		endofdocument = True
	finally:
		mytemplist = [charerror, ramount]
		fnametwo.seek(referind, 0)
		return mytemplist


# 3/18/21
def charfndr(schar, svar, qty):    # returns schar index history variable
	newlist = []
	try:
		#print(svar)
		scharind = svar.index(schar)
		newlist.append(scharind)
		lastind = newlist[len(newlist) - 1]
		nvar = svar[lastind + 1:]
		while qty > 1:
			scharind = nvar.index(schar)
			newlist.append(scharind)
			lastind = newlist[len(newlist) - 1]
			nvar = nvar[lastind + 1:]
			qty -= 1
	except Exception:# as charfndErr:
		pass
		#print(charfndErr)
	finally:
		return newlist


# 04/20/21      # PURPOSE: decind finder. makes things easier cuz I dont want to bug fix charfndr for decimals
def listcharfndr(schr, slvar):
	newlist = []
	for x in slvar:
		try:
			sind = x.index(schr)
			newlist.append(sind)
		except Exception:# as lcharErr:
			pass
			#print(lcharErr)
	return newlist


# 3/18/21 + 3/19/21     pulls into a hst var, every char before (but not including) a charsep in a string.
# noinspection PyGlobalUndefined
def stringsep(strvar, charsephst):
	try:
		startind = 0
		itemhst = []
		endind = 0
		tsvar = strvar
		for itemsep in charsephst:
			endind += itemsep + 1
			item = tsvar[startind:endind]
			itemhst.append(item[0:len(item) - 1])
			startind += itemsep + 1
		try:
			return itemhst
		except Exception:# as ssepErr:
			pass
			#print(ssepErr)
	except Exception:# as sepErr:
		pass
		#print(sepErr)


# 3/20/21   # this works. it removes a substring from a string in a list
def listchar_remover(listvar, oldchar):
	global charerror
	newlist = []
	charerror = False
	try:
		for item in listvar:
			oldcharind = item.index(oldchar)
			nitem = item[:oldcharind]
			nitem += item[oldcharind + 1:]
			newlist.append(nitem)
	except ValueError:
		charerror = True
	finally:
		return newlist


# 04/24/21  fixes errors in raw data in regards to multiple itemsep chars in a row
def itemsep_errfixer(isepchar, ritmstr):
	global charerror
	nstr = ''
	for i in ritmstr:
		if i == isepchar:
			if nstr[-1] == i:
				pass
			else:
				nstr += i
		else:
			nstr += i
	charerror = False
	return nstr


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # --- # 3/30/21 # --- # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def multimode(listvar): # something is happening here that makes it so I dont need multimodefndr()
	ssdict = {}
	for x in listvar:
		sskeylist = []
		sx = str(x)     # this finds all substring's in string and adds them to a list
		res = [sx[x:y] for x, y in combinations(
			range(len(sx) + 1), r=2)]
		for sub in res:     # this removes substring's that are 1 char in length
			if len(sub) == 1:
				res.remove(sub)
		for substring in res:
			if substring in sskeylist:      # makes sure we are not counting the same substring multiple times
				pass
			else:
				if len(substring) < 3:
					pass
				else:
					sskeylist.append(substring)
					sscunt = sx.count(substring)    # returns the amount of times a substring fits into a string
					try:        # eg; '40000' = string, '00' = substring, 2 = sscount. 40000
						oldvalue = ssdict[str(substring)]   # sscount = 2 because subs = 40, 00, 00, 00, 00.
						ssdict[str(substring)] = sscunt + oldvalue  # and string is parsed into = 4 00 00 / 40 00 0
					except Exception:
						ssdict[str(substring)] = sscunt

	return ssdict


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # --- # 4/04/21 # --- # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# I dont know how exatcly but this works. sorts dicts by value not key
def dict_value_sort(dictvar):
	sorted_dict = {}
	sorted_keys = sorted(dictvar, key=dictvar.get)

	for w in sorted_keys:
		sorted_dict[w] = dictvar[w]
	return sorted_dict


# returns the amount of times a modehopeful string occurs in a listvar's string that doesnt contain a modestring
def multimodefndr(modestring, modehopeful, listvar):
	modecnt = 0
	for x in listvar:
		if modestring in x:
			pass
		elif modehopeful in x:
			modecnt += 1
	return modecnt


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # --- # 4/05/21 # --- # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


# dictionary keys to list function
def dict_index(dvar):
	keyindlist = []
	for k in dvar.keys():
		keyindlist.append(str(k))
	return keyindlist


# bytesaved calculator
def savedspace(dictionaryvar):
	bsaved = {}
	for sskey in dictionaryvar.keys():
		sslen = len(sskey)
		savedbyte = (sslen - 1) * dictionaryvar[sskey]
		bsaved[sskey] = savedbyte
	return bsaved


def string_padder(schar1, schar2, padchar, slist):
	padded_list = []
	for x in slist:
		if schar1 in x:
			z = x
		elif schar2 in x:
			z = x
		else:
			y = len(x)
			if y not in [2, 4, 6, 8, 10, 12, 14, 16]:   # could go on longer if so desired
				z = padchar + x
			else:
				z = x
		padded_list.append(z)
	return padded_list


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # --- # 4/08/21 # --- # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


def runlength_list(listv):      # THIS SEEMS TO WORK !!!!!
	newlist = []
	tcunt = 0
	for x in range(1, len(listv)):
		if listv[x] == listv[x - 1]:
			tbool = True
			tcunt += 1
		else:
			tbool = False
			if tcunt > 0:
				tstr = listv[x - 1] + str(tcunt)
			else:
				tstr = listv[x - 1]
			newlist.append(tstr)
			tcunt = 0
		if x == len(listv) - 1:
			if tbool:
				if tcunt > 0:
					tstr = listv[x] + str(tcunt)
				else:
					tstr = listv[x]
				newlist.append(tstr)
			else:
				if tcunt > 0:
					tstr = listv[x] + str(tcunt)
				else:
					tstr = listv[x]
				newlist.append(tstr)
	if tcunt == len(listv) - 1:
		if tcunt <= 1:
			newlist.append(str(listv[0]))
		else:
			tstr = str(listv[0]) + '~' # or do str(tcunt)
			newlist.append(tstr)
	return newlist


def runlen_listcomp(numlistv):  # --04/24/21 this turns the number of the run into 1 char from two2one_compdict
	newlist = []
	tcunt = 0
	for x in range(1, len(numlistv)):
		if numlistv[x] == numlistv[x - 1]:
			tbool = True
			tcunt += 1
		else:
			tbool = False
			if tcunt > 0:
				xyz = str(tcunt)
				if len(xyz) < 2:
					xyz = '0' + xyz
				tstr = str(numlistv[x - 1]) + two2onedict[str(xyz)]
			else:
				tstr = str(numlistv[x - 1])
			newlist.append(tstr)
			tcunt = 0
		if x == len(numlistv) - 1:
			if tbool:
				xyz = str(tcunt)
				if len(xyz) < 2:
					xyz = '0' + xyz
				tstr = str(numlistv[x - 1]) + two2onedict[str(xyz)]
				newlist.append(tstr)
			else:
				if tcunt == 0:
					tstr = str(numlistv[x])
					newlist.append(tstr)
	if tcunt == len(numlistv) - 1:
		if tcunt <= 1:
			newlist.append(str(numlistv[0]))
		else:
			tstr = str(numlistv[0]) + '~'  # or do str(tcunt)
			newlist = [tstr]
	return newlist


# ~~~~~~~~~~ # |||||| # ~~~~~~~~~~ # |||||| # ~~~~~~~~~~ # |||||| # ~~~~~~~~~~ # |||||| # ~~~~~~~~~~ # |||||| # _______
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # --- # 4/19/21 # --- # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def newdictfunc(keynumv, keylistv, modvar, cleanblockhst):
	newdict = {}
	while keynumv > 0:  # dict iteration for finding alt mode hopefuls
		keynumv -= 1
		mhopeful = keylistv[keynumv]
		modecnt = multimodefndr(modvar, mhopeful, cleanblockhst)
		newdict[mhopeful] = modecnt
		# NOTE:: $control$ -04/23/21- ##$: this logic doesnt work due to main.py's function flow
		# $$$:: set up a boolean for if altmode can be found??
#		if modecnt > 0:
#			newdict[mhopeful] = modecnt
#		else:
#			pass
	return newdict


def mcitemblock(cleanblkhst, mvar, amvar, mstrings):
	mone = mstrings[0]  # finds location of mode or altmode in each item
	mtwo = mstrings[1]  # replaces mode chars with respective mode char
	newlist = []    # returns a list
	for i in cleanblkhst:
		if i == mvar:
			compitem = mone
		elif i == amvar:
			compitem = mtwo
		elif mvar in i:
			endind = len(mvar)# - 1
			raw = i[endind:]    # TODO:: is this only accounting for mode being first in the data set?
			compitem = mone + raw   # I think I might need a b4 ind w/ a endind and a try statement
		elif amvar in i:
			endind = len(amvar)# - 1
			raw = i[endind:]
			compitem = mtwo + raw
		else:
			compitem = i
		newlist.append(compitem)
	return newlist


def mcomppad(pcomplist, mstrgs, evennumbs):
	tlist = []
	mvar = mstrgs[0]
	amvar = mstrgs[1]
	for i in pcomplist:
		try:
			mind = i.index(mvar)
			# print(mind)
			if mind != 0:
				bstr = i[:mind]
				astr = i[mind + 1:]
				if len(bstr) not in evennumbs:
					bstr = '0' + bstr
				else:
					pass
				if len(astr) not in evennumbs:
					astr += '0'
				else:
					pass
				nstr = bstr + mvar + astr
				tlist.append(nstr)
			else:
				if len(i) in evennumbs:  # in case mode = first char but odd # of numbs follow
					i += '0'
				tlist.append(i)
		except Exception:
			try:
				amind = i.index(amvar)
				# print(amind)
				if amind != 0:
					bstr = i[:amind]
					astr = i[amind + 1:]
					if len(bstr) not in evennumbs:
						bstr = '0' + bstr
					else:
						pass
					if len(astr) not in evennumbs:
						astr += '0'
					else:
						pass
					nstr = bstr + amvar + astr
					tlist.append(nstr)
				else:
					if len(i) in evennumbs:  # in case mode = first char but odd # of numbs follow
						i += '0'
					tlist.append(i)
			except Exception:
				tlist.append(i)
		finally:
			pass
	return tlist


def plist2str(plist, mstrngs):
	templist = []
	for x in plist:
		tstring = ''
		for y in x:
			if y in mstrngs:
				templist.append(y)
			else:
				tstring += y
				if len(tstring) == 2:
					newstr = two2onedict[tstring]
					templist.append(newstr)
					tstring = ''
		templist.append(' ')
	return templist


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # --- # 4/23/21 # --- # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


def altmode_counter(amodv, clitemlist): # 04/24/21 -- used to make sure altmode occurs more than once
	tbool = False
	tcunt = 0
	for x in clitemlist:
		if amodv in x:
			tcunt += 1
		elif amodv == x:
			tcunt += 1
	if tcunt > 1:
		tbool = True
	return tbool


def num2str_comp(numv):     # turns num var <= 99,999,999,999 into str var for two2one comp
	xyz = str(numv)
	if len(xyz) in [1, 3, 5, 7, 9, 11]:
		xyz = '0' + str(numv)
	tstr = ''
	res = ''
	for x in xyz:
		tstr += x
		if len(tstr) == 2:
			res += two2onedict[tstr]
			tstr = ''
	return res


def simple_list2str(mylistv, myitemsepv):
	res = ''
	for x in mylistv:
		res += x + myitemsepv
	return res


# ~~~~~ |||:: these are self explaining. Very simple functions. ::||| ~~~~~ #


# ~~~~~~~~~~ # |||||| # ~~~~~~~~~~ # |||||| # ~~~~~~~~~~ # |||||| # ~~~~~~~~~~ # |||||| # ~~~~~~~~~~ # |||||| # _______


# NEW!!! This is for converting 2 byte numbers to 1 byte char's
two2onealpha = {
	'00': 'A', '01': 'B', '02': 'C', '03': 'D', '04': 'E', '05': 'F', '06': 'G', '07': 'H', '08': 'I', '09': 'J',
	'10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T',
	'20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z', '26': 'a', '27': 'b', '28': 'c', '29': 'd',
	'30': 'e', '31': 'f', '32': 'g', '33': 'h', '34': 'i', '35': 'j', '36': 'k', '37': 'l', '38': 'm', '39': 'n',
	'40': 'o', '41': 'p', '42': 'q', '43': 'r', '44': 's', '45': 't', '46': 'u', '47': 'v', '48': 'w', '49': 'x',
	'50': 'y', '51': 'z', '52': '!', '53': '@', '54': '#', '55': '$', '56': '%', '57': '^', '58': '&', '59': '*',
	'60': '(', '61': ')', '62': '│', '63': '┤', '64': '╡', '65': '╢', '66': '╖', '67': '╕', '68': '╣', '69': '║',
	'70': '╗', '71': '╝', '72': '╜', '73': '╛', '74': '┐', '75': '└', '76': '┴', '77': '┬', '78': '├', '79': '─',
	'80': '┼', '81': '╞', '82': '╟', '83': '╚', '84': '╔', '85': '╩', '86': '╦', '87': '╠', '88': '═', '89': '╬',
	'90': '╧', '91': '╨', '92': '╤', '93': '╥', '94': '╙', '95': '╘', '96': '╒', '97': '╓', '98': '╫', '99': '╪'
}


two2onedict = {
	'00': 'À', '01': 'Á', '02': 'Â', '03': 'Ã', '04': 'Ä', '05': 'Å', '06': 'Æ', '07': 'Ç', '08': 'È', '09': 'É',
	'10': 'Ê', '11': 'Ë', '12': 'Ì', '13': 'Í', '14': 'Î', '15': 'Ï', '16': 'Ð', '17': 'Ñ', '18': 'Ò', '19': 'Ó',
	'20': 'Ô', '21': 'Õ', '22': 'Ö', '23': 'Ø', '24': 'Ù', '25': 'Ú', '26': 'Û', '27': 'Ü', '28': 'Ý', '29': 'ß',
	'30': 'à', '31': 'á', '32': 'â', '33': 'ã', '34': 'ä', '35': 'å', '36': 'ç', '37': 'è', '38': 'é', '39': 'ê',
	'40': 'ë', '41': 'ì', '42': 'í', '43': 'î', '44': 'ï', '45': 'ð', '46': 'ñ', '47': 'ò', '48': 'ó', '49': 'ô',
	'50': 'õ', '51': 'ö', '52': 'ø', '53': 'ù', '54': 'ú', '55': 'û', '56': 'ü', '57': 'ý', '58': 'þ', '59': 'ÿ',
	'60': 'A', '61': 'B', '62': 'C', '63': 'D', '64': 'E', '65': 'F', '66': 'G', '67': 'H', '68': 'I', '69': 'J',
	'70': 'K', '71': 'L', '72': 'M', '73': 'N', '74': 'O', '75': 'P', '76': 'Q', '77': 'R', '78': 'S', '79': 'T',
	'80': 'U', '81': 'V', '82': 'W', '83': 'X', '84': 'Y', '85': 'Z', '86': 'a', '87': 'b', '88': 'c', '89': 'd',
	'90': 'e', '91': 'f', '92': 'g', '93': 'h', '94': 'i', '95': 'j', '96': 'k', '97': 'l', '98': 'm', '99': 'n'
}

