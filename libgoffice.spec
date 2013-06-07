%define		orgname	goffice

Summary:	Glib/Gtk+ set of document centric objects and utilities
Name:		libgoffice
Version:	0.10.2
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goffice/0.10/%{orgname}-%{version}.tar.xz
# Source0-md5:	74c20974c2cbbf60375c8a787e2b38c4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libgsf-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glib/Gtk+ set of document centric objects and utilities.

%package devel
Summary:	Header files for GOffice library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for GOffice.

%package apidocs
Summary:	libgoffice API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgoffice API documentation.

%prep
%setup -qn %{orgname}-%{version}

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-config-backend=gsettings	\
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}
%{__make} \
	DATADIRNAME=%{_datadir}	\

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/goffice/%{version}/plugins/*/*.la

%find_lang %{orgname}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{orgname}-%{version}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %ghost %{_libdir}/lib*.so.10
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%dir %{_libdir}/goffice
%dir %{_libdir}/goffice/%{version}
%dir %{_libdir}/goffice/%{version}/plugins
%dir %{_libdir}/goffice/%{version}/plugins/plot_barcol
%dir %{_libdir}/goffice/%{version}/plugins/plot_distrib
%dir %{_libdir}/goffice/%{version}/plugins/plot_pie
%dir %{_libdir}/goffice/%{version}/plugins/plot_radar
%dir %{_libdir}/goffice/%{version}/plugins/plot_surface
%dir %{_libdir}/goffice/%{version}/plugins/plot_xy
%dir %{_libdir}/goffice/%{version}/plugins/reg_linear
%dir %{_libdir}/goffice/%{version}/plugins/reg_logfit
%dir %{_libdir}/goffice/%{version}/plugins/smoothing

%attr(755,root,root) %{_libdir}/goffice/%{version}/plugins/*/*.so
%{_libdir}/goffice/%{version}/plugins/*/*.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
#%{_libdir}/lib*.la
%{_includedir}/libgoffice-0.10
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{orgname}-0.10

