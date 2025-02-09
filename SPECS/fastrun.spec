Name:           fastrun
Version:        0.1.0
Release:        1%{?dist}
Summary:        Fast command launcher tool for developers

License:        MIT
URL:            https://github.com/katoken03/fastrun
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang
Requires:       fzf

%description
A command launcher tool that helps developers run npm scripts and make targets 
without remembering exact command names.

%prep
%autosetup

%build
go build -o %{name} .

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
* Sun Feb 09 2025 katoken03 <your.email@example.com> - 1.0.0-1
- Initial RPM release