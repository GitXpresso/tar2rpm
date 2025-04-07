Name:           zen-browser
Version:        1.10
Release:        1%{?dist}
Source0:        zen.linux-x86_64.tar.xz
BuildArch:      x86_64
Summary:        More customizable browser

License:        MPL 2.0
URL:            http://zen-browser.app

%description
Zen browser now supports Fedora

%prep
%setup -n zen

%build
# You can include build commands here if needed, such as:
# ./configure
# make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/zen
mkdir -p %{buildroot}/usr/bin
cp -a . %{buildroot}/usr/share/zen
ln -s /usr/share/zen/zen %{buildroot}/usr/bin/zen
ln -s /usr/share/zen/zen-bin %{buildroot}/usr/bin/zen

%files
%defattr(-,root,root,-)
/usr/share/zen/*
/usr/bin/zen
/usr/bin/zen-bin
%changelog
* Mon Apr 07 2025 William <wg9797@outlook.com> - 1.10b-1
- Initial package.
