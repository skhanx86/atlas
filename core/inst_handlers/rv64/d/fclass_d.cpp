#include "core/inst_handlers/rv64/d/RvdInsts.hpp"
#include "core/ActionGroup.hpp"
#include "core/AtlasState.hpp"
#include "core/AtlasInst.hpp"

namespace atlas
{
    ActionGroup* RvdInsts::fclass_d_64_handler(atlas::AtlasState* state)
    {
        (void)state;
        ///////////////////////////////////////////////////////////////////////
        // START OF SPIKE CODE

        // require_either_extension('D', EXT_ZDINX);
        // require_fp;
        // WRITE_RD(f64_classify(FRS1_D));

        // END OF SPIKE CODE
        ///////////////////////////////////////////////////////////////////////
        return nullptr;
    }
} // namespace atlas