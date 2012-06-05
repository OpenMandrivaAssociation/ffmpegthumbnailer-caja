Summary:	Lightweight video thumbnailer
Name:		ffmpegthumbnailer-caja
Version:	1.2.0
Release:	1
License:	GPLv2+
Group:		Video
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz
Patch0:		ffmpegthumbnailer-caja_mateconf.patch
BuildArch:	noarch

%description
This package install a MateConf schemas to use ffmpegthumbnailer to
make thumbnails of video files in caja file manager.

%prep
%setup -q
%apply_patches

%build
%setup_compile_flags
%make

%install
%makeinstall_std

%files
%doc AUTHORS README
%{_sysconfdir}/mateconf/schemas/ffmpegthumbnailer-caja.schemas

