from from_root import from_root


def test_mkdirs(
        mock_get_project_root,
        tmp_path,
):
    project_dir = tmp_path / 'project'
    project_dir.mkdir()
    with (project_dir / '.project-root').open('w'):
        pass

    mock_get_project_root(
        [project_dir / 'module.py'],
        existing_paths=(),
        disable_exists_mock=True,
    )

    parents = 'dir1', 'dir2', 'dir3'

    path = from_root(*parents)
    assert not path.exists()

    path = from_root(*parents, mkdirs=True)
    assert path.exists()
    for i in range(len(parents) - 1):
        assert path.parents[i].is_dir()
