from conans import ConanFile, CMake


class MyLibConan(ConanFile):
    requires = ("boost/1.76.0")
    name = "a_project"
    license = "Some copyright 2022"
    author = "somebody@somewhere.com"
    url = "https://..."
    description = "A description"
    topics = ("some", "keywords")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"
    exports_sources = "*"
    options = {
        "boost_logging": [True, False],
    }
    default_options = {
        "boost_logging": True
    }

    def requirements(self):
        if self.options.boost_logging:
            self.requires("boost/1.76.0")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_EXPORT_COMPILE_COMMANDS"] = "ON"
        if self.options.boost_logging:
            cmake.definitions['BOOST_LOGGING'] = "ON"
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include/a_project", src="include")
        self.copy("*.hpp", dst="include/a_project", src="include")
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*-config.cmake", dst="lib", src="")

    def package_info(self):
        self.cpp_info.libs = ["a_project"]
