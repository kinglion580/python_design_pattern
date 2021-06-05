import os


class Process:
    def __init__(self, filename, base_ext, debug):
        self.__filename = filename
        self.__base_ext = base_ext
        self.__debug = debug

    def get_pn(self):
        pass

    def get_dst_dir(self):
        print('pn is ' + self.get_pn())
        print('查询目的路径')
        if self.__debug:
            print('替换目的路径')


class FileProcess(Process):

    def dieme(self, error):
        raise Exception(error)

    def get_base_ext_lst(self):
        print('获取文件正确后缀列表')
        return self.__base_ext.split('|')

    def get_ext(self):
        print('获取文件后缀')
        name, ext = os.path.splitext(self.__filename)
        return ext

    def verify_ext(self):
        print('判断文件后缀')
        ext = self.get_ext()
        if ext not in self.get_base_ext_lst():
            self.dieme('后缀不对')

    def get_name(self):
        name = os.path.splitext(self.__filename)[0]
        return name

    def get_pn(self):
        pass

    def verify_pn(self):
        pn = self.get_pn()
        if pn not in ['111', 'AAA']:
            self.dieme('pn not exist')

    def verify_release(self):
        print('判断是否已经发布')
        self.get_dst_dir()
        filename = self.__filename


class BrdFileProcess(FileProcess):

    def get_pn(self):
        name = self.get_name()
        pn = name.upper()
        print('获取pn')
        return pn

    def verify_lck(self):
        self.get_dst_dir()
        print('判断是否有lck文件')


class FabReadmeFileProcess(FileProcess):
    def set_pn(self):
        name = self.get_name()
        pn = name[0:2]
        print('获取pn')
        self.__pn = pn

    def verify_content(self):
        print('判断文件内容')


class FileProcessFactory:
    @staticmethod
    def create_file_process(filetype, filename, base_ext, debug):
        if filetype == 'PCB BRD':
            file_process = BrdFileProcess(filename, base_ext, debug)
        elif filetype == 'Fab':
            file_process = FabReadmeFileProcess(filename, base_ext, debug)
        return file_process


def test():
    try:
        file_process = FileProcessFactory.create_file_process('PCB BRD', '111.brd', '.brd', True)
        file_process.verify_ext()
        file_process.verify_pn()
        file_process.verify_release()
    except Exception as error:
        print(str(error))


