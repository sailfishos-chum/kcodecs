%global kf5_version 5.105.0

Name: opt-kf5-kcodecs
Version: 5.105.0
Release: 1%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with string manipulation methods

License:        GPLv2+ and LGPLv2+ and BSD
URL:            https://invent.kde.org/frameworks/kcodecs
Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires:  gperf
BuildRequires: opt-extra-cmake-modules >= %{kf5_version}
BuildRequires: opt-kf5-rpm-macros >= %{kf5_version}
BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-qt5-qttools-devel
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}

%description
KDE Frameworks 5 Tier 1 addon with string manipulation methods.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: opt-qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%find_lang_kf5 kcodecs5_qt


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_datadir}/qlogging-categories5/*categories
%{_opt_kf5_libdir}/libKF5Codecs.so.*
%{_opt_kf5_datadir}/locale/

%files devel

%{_opt_kf5_includedir}/KF5/KCodecs/
%{_opt_kf5_libdir}/libKF5Codecs.so
%{_opt_kf5_libdir}/cmake/KF5Codecs/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KCodecs.pri
