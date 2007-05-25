Summary:	Python bindings for Galago GTK
Summary(pl.UTF-8):	Wiązania Pythona do Galago GTK
Name:		python-galago-gtk
Version:	0.5.0
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://galago-project.org/files/releases/source/galago-gtk-python/galago-gtk-python-%{version}.tar.bz2
# Source0-md5:	3eb752eaa87d986bf272cf1266528c43
Patch0:		%{name}-codegen.patch
BuildRequires:	libgalago-gtk-devel >= 0.5.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-galago >= 0.5.0
BuildRequires:	python-pygtk-devel >= 2:2.4.0
BuildRequires:	rpm-pythonprov
Requires:	libgalago-gtk >= 0.5.0
Requires:	python-galago >= 0.5.0
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Galago GTK.

%description -l pl.UTF-8
Wiązania Pythona do Galago GTK.

%prep
%setup -q -n galago-gtk-python-%{version}
%patch0 -p1

%build
%configure
%{__make} \
	PYTHON="%{__python}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PYTHON="%{__python}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{py_sitedir}/gtk-2.0/galago
%attr(755,root,root) %{py_sitedir}/gtk-2.0/galago/*.so
%{_datadir}/pygtk/*/defs/galago-*.defs
%{_pkgconfigdir}/galago-gtk-python.pc
