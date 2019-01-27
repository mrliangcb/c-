5.选中物体
void Update () {
        Ray ray = Camera.main.ScreenPointToRay(Input.GetTouch(0).position);
        RaycastHit hit ;
        if (Physics.Raycast(ray, out hit))
        {

            Debug.Log("产生碰撞，并且碰撞体的名字是:"+hit.collider.name);
        }
        else {
            Debug.Log("没有碰撞");
        }
    }
