Summary:	A Linux clone of the QuickPict software that comes with the QuickCam
Name:		gqcam
Version:	0.9
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(cs):	X11/Aplikace/MultimÈdia
Group(da):	X11/Programmer/Multimedie
Group(de):	X11/Applikationen/Multimedien
Group(es):	X11/Aplicaciones/Multimedia
Group(fr):	X11/Applications/MultimÈdia
Group(is):	X11/Forrit/Margmilun
Group(it):	X11/Applicazioni/Multimedia
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•ﬁ•Î•¡•·•«•£•¢
Group(no):	X11/Programmer/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Group(pt):	X11/AplicaÁıes/MultimÈdia
Group(ru):	X11/“…Ãœ÷≈Œ…—/Ì’Ãÿ‘…Õ≈ƒ…¡
Group(sl):	X11/Programi/VeËpredstavnost
Group(sv):	X11/Till‰mpningar/Multimedia
Group(uk):	X11/“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Ì’Ãÿ‘…Õ≈ƒ¶¡
BuildRequires:	gtk+-devel libjpeg-devel libpng-devel
Source0:	http://cse.unl.edu/~cluening/gqcam/download/%{name}-%{version}.tar.bz2
URL:		http://cse.unl.edu/~cluening/gqcam/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gqcam allows you to use web cams with Linux.

Features:
  - Brightness Control
  - White Balance Control
  - Contrast Control
  - 3 Size Settings
  - 2 Depth Settings
  - Freeze Picture
  - Snap Picture (saves in png, ppm and jpeg format)
  - Command-line interface (good for webcam use)
  - Snapping on a timer
  - Support for the greyscale and color Quickcam, as well as CPiA based
    cameras and most any other driver that supports the read() command

The cameras the author have gotten gqcam to work with or have had
other people tell him it works with are:
  - Greyscale Quickcam
  - Color Quickcam

Anything listed below this line I have not tested and know very little
about:
  - Ezonics EZcam
  - Creative Web-Cam II
  - Philips USB PCVC675K
  - Webcam III
  - TerraCAM USB
  - Plustek OptiCam 300U

If you have gotten it work with a camera not listed here, feel free to
let him know at <cluenin1@bigred.unl.edu>

%prep

%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
install -m 755 gqcam $RPM_BUILD_ROOT/%{_bindir}/gqcam

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gqcam
%doc COPYING CHANGES INSTALL README README.threads
