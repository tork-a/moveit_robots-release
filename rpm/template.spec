Name:           ros-indigo-moveit-robots
Version:        1.0.6
Release:        0%{?dist}
Summary:        ROS moveit_robots package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/moveit_robots
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-atlas-moveit-config
Requires:       ros-indigo-atlas-v3-moveit-config
Requires:       ros-indigo-baxter-ikfast-left-arm-plugin
Requires:       ros-indigo-baxter-ikfast-right-arm-plugin
Requires:       ros-indigo-baxter-moveit-config
Requires:       ros-indigo-clam-moveit-config
Requires:       ros-indigo-r2-moveit-generated
BuildRequires:  ros-indigo-catkin

%description
moveit_robots meta-package contains multiple robots moveit configuration
packages.

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
* Tue Apr 19 2016 Sachin Chitta <robot.moveit@gmail.com> - 1.0.6-0
- Autogenerated by Bloom

* Wed Feb 10 2016 Sachin Chitta <robot.moveit@gmail.com> - 1.0.5-0
- Autogenerated by Bloom

* Fri Jan 15 2016 Sachin Chitta <robot.moveit@gmail.com> - 1.0.4-0
- Autogenerated by Bloom

* Mon Nov 02 2015 Sachin Chitta <robot.moveit@gmail.com> - 1.0.3-0
- Autogenerated by Bloom

* Sat Sep 19 2015 Sachin Chitta <robot.moveit@gmail.com> - 1.0.2-0
- Autogenerated by Bloom

