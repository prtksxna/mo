#!/usr/bin/env python
# coding=utf8

import sys

momo = {
	"headphones": "d(*_*)b",
	"bigheadphones": "O(*+*)O",
	"cthulhu": "^(;,;)^",
	"wavedance": "(〜￣▽￣)〜",
	"wavedancerev": "〜(￣▽￣〜)",
	"sadblame": "(;´・`)>",
	"tantrum": "＼(｀0´)／",
	"crying": "(ू˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ू)",
	"yawn": "ᕙ(⇀‸↼‶)ᕗ",
	"dead": "╭( ✖_✖ )╮",
	"dancespin": "ヘ( ^o^)ノ＼(^_^ )",
	"boohoo": "(ू˃̣̣̣̣̣̣o˂̣̣̣̣̣̣ ू)⁼³₌₃",
	"rain": "⁝⁞⁝⁞ʕु•̫͡•ʔु☂⁝⁞⁝⁝",
	"bow": "(シ_ _)シ",
	"cryexplain": "_:(´□`」 ∠):_",
	"nyam": "( ͒ ु- •̫̮ – ू ͒)",
	"dancegroup": "\(._.\) ƪ(‘-’ ƪ)(ʃ ‘-’)ʃ (/._.)/",
	"dancesnap": "ヾ(-_- )ゞ",
	"yayjump": "o(〃＾▽＾〃)o",
	"chai": "( -_-)旦~",
	"food": "( ˘▽˘)っ♨",
	"party": "(º﹃º):.*೨",
	"hug": "(>^_^)><(^o^<)",
	"hugkiss": "(づ￣ ³￣)づ",
	"meh": "ヽ(ー_ー )ノ",
	"fight": "Ｏ( ｀_´)乂(｀_´ )Ｏ",
	"stickup": "(҂‾ ▵‾)︻デ═一 \(˚▽˚’!)/",
	"yum": "(っ˘ڡ˘ς)",
	"overhere": "〈(•ˇ‿ˇ•)-→",
	"saddream": "(  ु⁎ᴗ_ᴗ⁎)ु.｡oO",
	"wave": "ヾ(＾-＾)ノ",
	"zzz": "(-, – )…zzZZ"
}

if __name__ == '__main__':
	mo = sys.argv[2]
	if mo in momo:
		text = " ".join( sys.argv[3:] ) if len( sys.argv ) >= 4 else ""
		print momo[ mo ] + " " + text
	elif mo == "list":
		for name in momo:
			print "/debug " + name + "\t" + momo[ name ]
	else:
		commands = ", ".join( momo.keys() )
		print "/debug Use '/mo [command] your text'. Use '/mo list' too see all emoticons. Commands: " + commands
