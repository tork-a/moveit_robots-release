Name:           ros-indigo-atlas-v3-moveit-config
Version:        1.0.4
Release:        0%{?dist}
Summary:        ROS atlas_v3_moveit_config package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-atlas-moveit-config
Requires:       ros-indigo-moveit-ros-move-group
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-atlas-moveit-config
BuildRequires:  ros-indigo-catkin

%description
An automatically generated package with all the configuration and launch files
for using the atlas with the MoveIt Motion Planning Framework

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Jan 15 2016 MoveIt Setup Assistant <assistant@moveit.ros.org> - 1.0.4-0
- Autogenerated by Bloom

* Mon Nov 02 2015 MoveIt Setup Assistant <assistant@moveit.ros.org> - 1.0.3-0
- Autogenerated by Bloom

* Sat Sep 19 2015 MoveIt Setup Assistant <assistant@moveit.ros.org> - 1.0.2-0
- Autogenerated by Bloom

