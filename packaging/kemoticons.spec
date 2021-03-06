# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kemoticons

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 3 module for emoticons support
Version:    5.3.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kemoticons.yaml
Source101:  kemoticons-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  karchive-devel
BuildRequires:  kconfig-devel
BuildRequires:  kservice-devel

%description
KDE Frameworks 5 Tier 3 module for emoticons support


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   karchive-devel
Requires:   kconfig-devel
Requires:   kservice-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5Emoticons.so.*
%{_kf5_plugindir}/*
%{_kf5_servicesdir}/*
%{_kf5_servicetypesdir}/*
%{_kf5_sharedir}/emoticons/Glass
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/kemoticons_version.h
%{_kf5_includedir}/KEmoticons
%{_kf5_libdir}/libKF5Emoticons.so
%{_kf5_cmakedir}/KF5Emoticons
%{_kf5_mkspecsdir}/qt_KEmoticons.pri
# >> files devel
# << files devel
