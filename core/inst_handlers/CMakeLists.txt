project(Atlas)

add_subdirectory(i)
add_subdirectory(m)
add_subdirectory(a)
add_subdirectory(f)
add_subdirectory(d)
add_subdirectory(zicsr)
add_subdirectory(zifencei)

add_library(atlasinsts)
target_link_libraries(atlasinsts
    rvi
    rvm
    rva
    rvf
    rvd
    rvzicsr
    rvzifencei
)
add_dependencies(atlasinsts AutogenArchFiles)
