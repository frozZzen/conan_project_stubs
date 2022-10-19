from conans import ConanFile, CMake

class MmlConan(ConanFile):
    name = a_project"
    license = "Some copyright 2022"
    author = "somebody@somewhere.com"
    url = "https://..."
    description = "A description"
    topics = ("some", "keywords")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include/a_project", src="include")
        self.copy("*.hpp", dst="include/a_project", src="include")
        self.copy("*-config.cmake", dst="lib", src="")

    def package_info(self):
        self.info.header_only()
