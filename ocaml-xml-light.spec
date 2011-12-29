%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%global debug_package %{nil}

Name:           ocaml-xml-light
Version:        2.2.cvs20070817
Release:        13.2%{?dist}
Summary:        Minimal XML parser and printer for OCaml

Group:          Development/Libraries
License:        LGPLv2+
URL:            http://tech.motion-twin.com/xmllight.html
Source0:        xml-light-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 3.10.1
BuildRequires:  ocaml-findlib-devel, ocaml-ocamldoc
BuildRequires:  gawk

%description
Xml-Light is a minimal XML parser & printer for OCaml. It provides
functions to parse an XML document into an OCaml data structure, work
with it, and print it back to an XML document. It support also DTD
parsing and checking, and is entirely written in OCaml, hence it does
not require additional C library.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -c -q -n xml-light-%{version}


%build
make all doc
%if %opt
make opt
%endif
sed -e 's/@VERSION@/%{VERSION}/' < META.in > META


%install
rm -rf $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
rm -f test.cmi
ocamlfind install xml-light META *.mli *.cmi *.cma *.a *.cmxa *.cmx


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/ocaml/xml-light
%if %opt
%exclude %{_libdir}/ocaml/xml-light/*.a
%exclude %{_libdir}/ocaml/xml-light/*.cmxa
%exclude %{_libdir}/ocaml/xml-light/*.cmx
%endif
%exclude %{_libdir}/ocaml/xml-light/*.mli


%files devel
%defattr(-,root,root,-)
%doc README doc/*
%if %opt
%{_libdir}/ocaml/xml-light/*.a
%{_libdir}/ocaml/xml-light/*.cmxa
%{_libdir}/ocaml/xml-light/*.cmx
%endif
%{_libdir}/ocaml/xml-light/*.mli


%changelog
* Mon Jan 11 2010 Richard W.M. Jones <rjones@redhat.com> - 2.2.cvs20070817-13.2
- Replace %%define with %%global.
- Use upstream RPM 4.8 OCaml dependency generator.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.2.cvs20070817-13.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.cvs20070817-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.2.cvs20070817-12
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.cvs20070817-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.cvs20070817-10
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.cvs20070817-9
- Rebuild for OCaml 3.11.0

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.cvs20070817-8
- Rebuild for OCaml 3.10.2

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.cvs20070817-7
- Rebuild for ppc64.

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 2.2.cvs20070817-6
- Rebuild for OCaml 3.10.1

* Thu Sep  6 2007 Richard W.M. Jones <rjones@redhat.com> - 2.2.cvs20070817-5
- Don't package test.cmi file (it's a test program).

* Thu Sep  6 2007 Richard W.M. Jones <rjones@redhat.com> - 2.2.cvs20070817-4
- Force rebuild because of updated requires/provides scripts in OCaml.

* Thu Aug 30 2007 Richard W.M. Jones <rjones@redhat.com> - 2.2.cvs20070817-3
- Force rebuild because of changed BRs in base OCaml.

* Fri Aug 24 2007 Richard W.M. Jones <rjones@redhat.com> - 2.2.cvs20070817-2
- Clarified that the license is LGPLv2+.

* Fri Aug 17 2007 Richard W.M. Jones <rjones@redhat.com> - 2.2.cvs20070817-1
- Initial RPM release.
