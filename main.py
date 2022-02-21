import os
import re

allpath = []
allname = []


def getallfile(path):
    allfilelist = os.listdir(path)
    # 遍历该文件夹下的所有目录或者文件
    for file in allfilelist:
        filepath = os.path.join(path, file)
        # 如果是文件夹，递归调用函数
        if os.path.isdir(filepath):
            getallfile(filepath)
        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(filepath):
            allpath.append(filepath)
            allname.append(file)
    return allpath, allname


def re_get_core(namelist):
    for e in namelist:
        origin = e
        e = e.replace('.txt', '')
        match_flag = False
        pattern = [r'(?:「)(.*)(?:」)',
                   r'(?:你|你们)(?:喜欢|读过|听过|有哪些|喜欢|心目中|最喜欢|知道|见过|觉得|认为)(?:的)?(?:哪些|一句|有哪些)?(?:写得最好的)?(?:最能)?(?:关于|形容|体现|表达)?(.*)(?:的诗句|的古诗|的诗|的一句诗)',
                   r'(.*?)用?诗句(?:怎么)?表达',
                   r'(?:一些|一句|哪些)?(?:关于)?(.*)的[古诗|诗句]',
                   r'(?:一句|一首|哪些)?(?:你心目中)?(?:古诗词|诗)?(?:表达出|形容|表达|描述)(.*)(?:的诗)|',
                   r'(.*)你想到诗句有哪些',
                   r'^什么(?:诗句)?(.*)',
                   r'关于(.*)，',
                   r'(?:古代|古诗中)(?:有)?(?:哪些)?(?:描述|形容|很)(.*)(?:的诗)']
        # 要匹配的最短的一个
        e_match_result = []
        for each in pattern:
            result = re.findall(each, e)
            if result:
                match_flag = True
                core = result[0]
                if not core:
                    continue
                allsign = "，？"
                for i in allsign:
                    core = core.replace(i, '')
                e_match_result.append(core)
        try:
            e_result = min(e_match_result, key=len)
            e_result = e_result.replace('」「', ',').replace('」或「', ',')
            print(origin + ' ===> ' + e_result)
        except:
            pass
        if not match_flag:
            print(origin + ' --- not match')



if __name__ == "__main__":
    rootdir = "res"
    # file是带路径的，names是单纯的文件名
    files, names = getallfile(rootdir)
    print(names)
    re_get_core(names)

