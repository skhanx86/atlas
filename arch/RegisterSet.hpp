#pragma once

#include "sparta/functional/RegisterSet.hpp"
#include "arch/RegisterDefnsJSON.hpp"
#include "include/AtlasTypes.hpp"
#include "include/CSRBitMasks64.hpp"

namespace atlas
{

class RegisterSet : public sparta::RegisterSet
{
public:
    RegisterSet(sparta::TreeNode *parent,
                std::unique_ptr<RegisterDefnsFromJSON> defns,
                const std::string& name = "regs")
        : sparta::RegisterSet(parent,
                              defns->getAllDefns(),
                              sparta::RegisterSet::RegisterTypeTag<sparta::Register>(),
                              name)
    {
        defs_from_json_ = std::move(defns);

        sparta::RegisterBase::ident_type max_reg_id = 0;
        for (uint32_t i = 0; i < defs_from_json_->getNumDefns(); ++i) {
            sparta::RegisterBase::Definition *def = defs_from_json_->getAllDefns() + i;
            max_reg_id = std::max(max_reg_id, def->id);
        }

        registers_by_reg_num_.resize(max_reg_id + 1, nullptr);
        for (uint32_t i = 0; i < defs_from_json_->getNumDefns(); ++i) {
            sparta::RegisterBase::Definition *def = defs_from_json_->getAllDefns() + i;
            auto reg_name = def->name;
            auto reg = sparta::RegisterSet::getRegister(reg_name);

            sparta_assert(registers_by_reg_num_[def->id] == nullptr,
                          "Register number " << def->id << " is not unique");

            registers_by_reg_num_[def->id] = dynamic_cast<sparta::Register*>(reg);
        }
    }

    static std::unique_ptr<RegisterSet>
    create(sparta::TreeNode *parent, const std::string& register_defns_json, const std::string& name = "regs")
    {
        auto defns = std::make_unique<RegisterDefnsFromJSON>(register_defns_json);
        return std::make_unique<RegisterSet>(parent, std::move(defns), name);
    }

    static std::unique_ptr<RegisterSet>
    create(sparta::TreeNode *parent, const std::vector<std::string>& register_defns_jsons, const std::string& name = "regs")
    {
        auto defns = std::make_unique<RegisterDefnsFromJSON>(register_defns_jsons);
        return std::make_unique<RegisterSet>(parent, std::move(defns), name);
    }

    sparta::Register *getRegister(uint32_t reg_num)
    {
        #ifdef NDEBUG
            return registers_by_reg_num_[reg_num];
        #else
            return registers_by_reg_num_.at(reg_num);
        #endif
    }

    // Bring in getRegister(const char* reg_name) from sparta::RegisterSet
    using sparta::RegisterSet::getRegister;

    template <typename T>
    inline void writeRegister(uint32_t reg_num, T reg_value, uint32_t idx = 0)
    {
        getRegister(reg_num)->write<T>(reg_value, idx);
    }

    template <typename T>
    inline T readRegister(uint32_t reg_num, uint32_t idx = 0)
    {
        return getRegister(reg_num)->read<T>(idx);
    }

private:
    /*!
     * \brief Register definitions parsed from JSON file(s). We have to hold onto
     * this to keep the definitions alive, specifically the various strings that
     * are held by the register/field definitions as a const char* (e.g. group
     * name, field name, etc.)
     */
    std::unique_ptr<RegisterDefnsFromJSON> defs_from_json_;

    /*!
     * \brief Vector of definitions for the registers in this set. The index of
     * the entries in this vector correspond to the register number seen in the
     * JSON file(s).
     */
    std::vector<sparta::Register*> registers_by_reg_num_;
};

} // namespace atlas