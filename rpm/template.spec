Name:           ros-indigo-baxter-ikfast-right-arm-plugin
Version:        1.0.6
Release:        0%{?dist}
Summary:        ROS baxter_ikfast_right_arm_plugin package

Group:          Development/Libraries
License:        BSD
URL:            http://www.rethinkrobotics.com/sdk
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cmake-modules
Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf-conversions
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf-conversions

%description
The baxter_ikfast_right_arm_plugin package

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Tue Apr 19 2016 Rethink Robotics Inc. <rsdk.support@rethinkrobotics.com> - 1.0.6-0
- Autogenerated by Bloom

* Wed Feb 10 2016 Rethink Robotics Inc. <rsdk.support@rethinkrobotics.com> - 1.0.5-0
- Autogenerated by Bloom

* Fri Jan 15 2016 Rethink Robotics Inc. <rsdk.support@rethinkrobotics.com> - 1.0.4-0
- Autogenerated by Bloom

* Mon Nov 02 2015 Rethink Robotics Inc. <rsdk.support@rethinkrobotics.com> - 1.0.3-0
- Autogenerated by Bloom

* Sat Sep 19 2015 Rethink Robotics Inc. <rsdk.support@rethinkrobotics.com> - 1.0.2-0
- Autogenerated by Bloom

