# TODO
# - v4l1 patch needed
Summary:	A Linux clone of the QuickPict software that comes with the QuickCam
Summary(pl.UTF-8):	Linuksowy klon oprogramowania QuickPict przychodzącego z QuickCam
Name:		gqcam
Version:	0.9.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.debian.org/debian/pool/main/g/gqcam/%{name}_%{version}.orig.tar.gz
# Source0-md5:	d1f2eecec0dbd4dd88543986b47e2015
Patch0:		ftp://ftp.debian.org/debian/pool/main/g/gqcam/%{name}_%{version}-4.diff.gz
# Patch0-md5:	7ab126a358fe2147a9f5a217b8b99c6c
URL:		http://cse.unl.edu/~cluening/gqcam/
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Gqcam pozwala na używanie kamer internetowych pod Linuksem.

Możliwości: kontrola jasności, kontrastu i balansu bieli, 3 ustawienia
rozmiaru, 2 ustawienia głębi, zamrażanie obrazu, zrzucanie obrazu (do
formatu PNG, PPM lub JPEG) - także sterowane timerem, interfejs z
linii poleceń, obsługa czarno-białych i kolorowych kamer QuickCam, a
także kamer opartych na CPiA oraz większości innych obsługujących
polecenie read().

Kamery o których wiadomo, że działają, to: Greyscale Quickcam i Color
Quickcam; nie były testowane: Ezonics EZcam, Creative Web-Cam II,
Philips USB PCVC675K, Webcam III, TerraCAM USB, Plustek OptiCam 300U.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}" \
	LD="%{__cc} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p gqcam $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL README README.threads
%attr(755,root,root) %{_bindir}/gqcam
