Summary:	Lightweight video thumbnailer
Name:		ffmpegthumbnailer-caja
Version:	1.4.0
Release:	2
License:	GPLv2+
Group:		Video
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
Patch0:		ffmpegthumbnailer-caja_mateconf.patch
BuildArch:	noarch

%description
This package install a MateConf schemas to use ffmpegthumbnailer to
make thumbnails of video files in caja file manager.

%prep
%setup -q
%autopatch -p1

%build
%setup_compile_flags
%make

%install
%makeinstall_std

%files
%doc AUTHORS README
%{_sysconfdir}/mateconf/schemas/ffmpegthumbnailer-caja.schemas



%changelog
* Tue Jun 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 802762
- imported package ffmpegthumbnailer-caja

