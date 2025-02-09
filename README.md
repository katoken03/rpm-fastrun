# rpm-fastrun

RPM package for fastrun command launcher

## Building locally

1. Install build dependencies:
```bash
sudo dnf install rpm-build rpmdevtools golang git make
```

2. Set up RPM build environment:
```bash
rpmdev-setuptree
cp SPECS/fastrun.spec ~/rpmbuild/SPECS/
```

3. Build the RPM:
```bash
rpmbuild -ba ~/rpmbuild/SPECS/fastrun.spec
```

The built RPM will be in `~/rpmbuild/RPMS/x86_64/`.

## Installation

```bash
sudo dnf install fastrun-1.0.0-1.fc*.x86_64.rpm
```
